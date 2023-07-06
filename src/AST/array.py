from src.AST.data import *
from src.AST_Base import *
from src.error import *
from src.global_var import *

class Array(AST_Node):
    def __init__(self, id, dimensions, type, *args, **kwargs):
        self.type = 'ARRAY'
        self.id = id
        self.var_type = type
        self.dimensions = dimensions
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + self.dimensions.get_tree(level + 1) + '\n' + LEVEL_STR * (level+1) + str(self.var_type)

    def add_variables(self, dimensions):
        result = {}
        if len(dimensions) == 1:
            for i in range(dimensions[0][0], dimensions[0][1]+1):
                result[i] = (stack.structs[self.var_type](), self.var_type)
        else:
            d = self.add_variables(dimensions[1:])
            for i in range(dimensions[0][0], dimensions[0][1]+1):
                result[i] = (d.copy(), 'ARRAY')
        return result

    def exe(self):
        dimensions = self.dimensions.exe()
        result = self.add_variables(dimensions)
        stack.new_variable(self.id, 'ARRAY')
        stack.set_variable(self.id, result, 'ARRAY')

class Dimensions(AST_Node):
    def __init__(self, *args, **kwargs):
        self.type = 'DIMENSIONS'
        self.dimensions = []
        super().__init__(*args, **kwargs)

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
        self.type = 'DIMENSION'
        self.left = left
        self.right = right
        super().__init__(*args, **kwargs)

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
        self.type = 'ARRAY_ASSIGN'
        self.id = id
        self.indexes = indexes
        self.value = value
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + self.indexes.get_tree(level+1) + '\n' + self.value.get_tree(level+1)

    def set_value(self, arr, index, value):
        if len(index) == 1:
            index = index[0]
            try:
                arr[index] = (stack.structs[arr[index][1]](value[0]), arr[index][1])
            except:
                add_error_message(f'Cannot assign `{value[1]}` to `{arr[index][1]}`. ', self)
        else:
            self.set_value(arr[index[0]], index[1:], value)

    def exe(self):
        indexes = self.indexes.exe()
        value = self.value.exe()
        arr = stack.get_variable(self.id)[0]
        self.set_value(arr, indexes, value)

        stack.set_variable(self.id, arr, 'ARRAY')

class Indexes(AST_Node):
    def __init__(self, *args, **kwargs):
        self.type = 'INDEXES'
        self.indexes = []
        super().__init__(*args, **kwargs)

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
        self.type = 'ARRAY_GET'
        self.id = id
        self.indexes = indexes
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + self.indexes.get_tree(level+1)

    def get_value(self, arr, index):
        if len(index) == 1:
            return arr[index[0]][0]
        else:
            return self.get_value(arr[index[0]], index[1:])

    def exe(self):
        indexes = self.indexes.exe()
        arr = stack.get_variable(self.id)[0]
        value = self.get_value(arr, indexes)
        return value
