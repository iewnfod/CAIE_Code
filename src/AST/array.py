from .data import *
from ..AST_Base import *
from ..error import *
from ..global_var import *
from ..data_types import ARRAY
from copy import copy

class Array(AST_Node):
    def __init__(self, id, dimensions, type, private=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'ARRAY'
        self.id = id
        self.dimensions = dimensions
        self.var_type = type
        self.private = private

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + self.dimensions.get_tree(level + 1) + '\n' + LEVEL_STR * (level+1) + str(self.var_type) + '\n' + LEVEL_STR * (level+1) + str(self.private)

    def add_variables(self, dimensions):
        result = {}
        result['left'] = dimensions[0][0]
        result['right'] = dimensions[0][1]
        if len(dimensions) == 1:
            for i in range(dimensions[0][0], dimensions[0][1]+1):
                result[i] = (stack.structs[self.var_type](name=i), self.var_type)
        else:
            for i in range(dimensions[0][0], dimensions[0][1]+1):
                result[i] = (ARRAY(self.add_variables(dimensions[1:])), 'ARRAY')
        return result

    def exe(self):
        dimensions = self.dimensions.exe()
        result = self.add_variables(dimensions)
        stack.new_variable(self.id, 'ARRAY', result)
        if self.private:
            stack.get_variable(self.id).current_space = stack.current_space()

class Dimensions(AST_Node):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'DIMENSIONS'
        self.dimensions = []

    def get_tree(self, level=0):
        r = LEVEL_STR * level + self.type
        for i in self.dimensions:
            r += '\n' + i.get_tree(level+1)
        return r

    def add_dimension(self, dimension):
        self.dimensions.append(dimension)

    def exe(self):
        result = []
        for dimension in self.dimensions:
            result.append(dimension.exe())
        return result

class Dimension(AST_Node):
    def __init__(self, left, right, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'DIMENSION'
        self.left = left
        self.right = right

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level+1) + '\n' + self.right.get_tree(level+1)

    def exe(self):
        left = self.left.exe()
        right = self.right.exe()
        if left[1] == 'INTEGER' and right[1] == 'INTEGER':
            return (left[0], right[0])
        else:
            add_error_message(f'Array dimension should be INTEGER, but found {left[0]} and {right[0]}', self)

class Array_assign(AST_Node):
    def __init__(self, id, indexes, value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'ARRAY_ASSIGN'
        self.id = id
        self.indexes = indexes
        self.value = value

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + self.indexes.get_tree(level+1) + '\n' + self.value.get_tree(level+1)

    def set_value(self, arr, index, value):
        if len(index) == 1:
            index = index[0]
            if index not in arr:
                add_error_message(f'Array index `{index}` out of bounds', self)
                return
            try:
                arr[index][0].set_value(value[0])
            except:
                add_error_message(f'Cannot assign `{value[1]}` to `{arr[index][1]}`', self)
        else:
            self.set_value(arr[index[0]][0][0], index[1:], value)

    def exe(self):
        indexes = self.indexes.exe()
        value = self.value.exe()
        arr = stack.get_variable(self.id)[0]
        self.set_value(arr, indexes, value)

        stack.set_variable(self.id, arr, 'ARRAY')

class Indexes(AST_Node):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'INDEXES'
        self.indexes = []

    def get_tree(self, level=0):
        result = LEVEL_STR * level + self.type
        for i in self.indexes:
            result += '\n' + i.get_tree(level+1)
        return result

    def add_index(self, index):
        self.indexes.append(index)

    def exe(self):
        index_list = []
        for index in self.indexes:
            r = index.exe()
            if r[1] == 'INTEGER':
                index_list.append(r[0])
        return index_list

class Array_get(AST_Node):
    def __init__(self, id, indexes, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'ARRAY_GET'
        self.id = id
        self.indexes = indexes

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + self.indexes.get_tree(level+1)

    def get_value(self, arr, index):
        if len(index) == 1:
            if index[0] in arr.keys():
                return arr[index[0]][0]
            else:
                add_error_message(f'Array index `{index[0]}` out of bounds', self)
        else:
            return self.get_value(arr[index[0]][0][0], index[1:])

    def exe(self):
        indexes = self.indexes.exe()
        arr = stack.get_variable(self.id)[0]
        value = self.get_value(arr, indexes)
        return value

class Array_items(AST_Node):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'ARRAY_ITEMS'
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_tree(self, level=0):
        return LEVEL_STR* level + self.type + '\n' + '\n'.join(i.get_tree(level+1) for i in self.items)

    def exe(self):
        items = []
        for i in self.items:
            items.append(i.exe())
        return items

class Array_expression(AST_Node):
    def __init__(self, items, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'ARRAY_EXPRESSION'
        self.items = items

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.items.get_tree(level+1)

    def exe(self):
        value = {}
        items = self.items.exe()
        value['left'] = 1
        value['right'] = len(items)
        if items:
            type_l = set()
            for i in range(1, len(items)+1):
                if type(items[i-1]) == tuple:
                    value[i] = (stack.structs[items[i-1][1]](items[i-1][0]), items[i-1][1])
                else:
                    value[i] = (copy(items[i-1]), items[i-1][1])
                type_l.add(value[i][1])
            # 如果有多种类型，set就不会是1
            if len(type_l) > 1:
                add_error_message('There should not be more than one type of value in a array', self)
        return ARRAY(value)
