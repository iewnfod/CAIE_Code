from src.AST.data import *

class Output:
    def __init__(self, value):
        self.type = 'OUTPUT'
        self.value = value

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.value.get_tree(level+1)

    def exe(self):
        print(self.value.exe())

class Output_expression:
    def __init__(self):
        self.type = 'OUTPUT_EXPRESSION'
        self.expressions = []

    def get_tree(self, level=0):
        r = LEVEL_STR * level + self.type
        for i in self.expressions:
            r += '\n' + i.get_tree(level+1)
        return r

    def add_expression(self, expression):
        self.expressions.append(expression)

    def exe(self):
        result = ''
        for i in self.expressions:
            t = i.exe()
            if t[1] == 'BOOLEAN':
                result += str({True: 'TRUE', False: 'FALSE', None: 'None'}[t[0]])
            else:
                result += str(t[0])
        return result

class Input:
    def __init__(self, id):
        self.type = 'INPUT'
        self.id = id

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id)

    def exe(self):
        stack.set_variable(self.id, str(input()), 'STRING')

class Array_input:
    def __init__(self, id, indexes):
        self.type = 'ARRAY_INPUT'
        self.id = id
        self.indexes = indexes

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + str(self.id) + '\n' + self.indexes.get_tree(level+1)

    def exe(self):
        indexes = self.indexes.exe()
        target_id = self.id
        for index in indexes:
            target_id += '.' + str(index)
        stack.set_variable(target_id, str(input()), 'STRING')
