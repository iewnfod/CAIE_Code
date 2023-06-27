from src.AST.data import *

class Array:
    def __init__(self, id, dimensions, type):
        self.type = 'ARRAY'
        self.id = id
        self.var_type = type
        self.dimensions = dimensions

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + str(self.id) + '\n' + self.dimensions.get_tree(level + 1) + '\n' + str(self.var_type)

    # 通过.来表达从属关系，然后推入stack
    def add_variables(self, base_name, dimensions):
        if len(dimensions) == 1:
            for i in range(dimensions[0][0], dimensions[0][1]+1):
                stack.new_variable(f'{base_name}.{i}', self.var_type)
        else:
            for i in range(dimensions[0][0], dimensions[0][1]+1):
                self.add_variables(f'{base_name}.{i}', dimensions[1:])

    def exe(self):
        dimensions = self.dimensions.exe()
        self.add_variables(self.id, dimensions)

class Dimensions:
    def __init__(self):
        self.type = 'DIMENSIONS'
        self.dimensions = []

    def get_tree(self, level=0):
        r = LEVEL_STR * level + self.type
        for i in self.dimensions:
            r += '\n' + i.get_tree(level+1)

    def add_dimension(self, dimension):
        self.dimensions.append(dimension)

    def exe(self):
        result = []
        for dimension in self.dimensions:
            result.append(dimension.exe())
        return result

class Dimension:
    def __init__(self, left, right):
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
            print('Array dimension should be INTEGER. ')

class Array_assign:
    def __init__(self, id, indexes, value):
        self.type = 'ARRAY_ASSIGN'
        self.id = id
        self.indexes = indexes
        self.value = value

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + str(self.id) + '\n' + self.indexes.get_tree(level+1) + '\n' + self.value.get_tree(level+1)

    def exe(self):
        indexes = self.indexes.exe()
        value = self.value.exe()
        target_id = self.id
        for i in indexes:
            target_id += '.' + str(i)
        stack.set_variable(target_id, value[0], value[1])

class Indexes:
    def __init__(self):
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

class Array_get:
    def __init__(self, id, indexes):
        self.type = 'ARRAY_GET'
        self.id = id
        self.indexes = indexes
        self.result = {}

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + str(self.id) + '\n' + self.indexes.get_tree(level+1) + '\n' + self.value.get_tree(level+1)

    def exe(self):
        indexes = self.indexes.exe()
        target_id = self.id
        for index in indexes:
            target_id += '.' + str(index)
        return stack.get_variable(target_id)
