from src.AST.data import *
from src.AST_Base import *
from src.error import *
from src.status import *

class Output(AST_Node):
    def __init__(self, value, *args, **kwargs):
        self.type = 'OUTPUT'
        self.value = value
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.value.get_tree(level+1)

    def exe(self):
        print(self.value.exe())

class Output_expression(AST_Node):
    def __init__(self, *args, **kwargs):
        self.type = 'OUTPUT_EXPRESSION'
        self.expressions = []
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        r = LEVEL_STR * level + self.type
        for i in self.expressions:
            r += '\n' + i.get_tree(level+1)
        return r

    def add_expression(self, expression):
        self.expressions.append(expression)

    def get_str(self, value):
        if value[1] == 'BOOLEAN':
            return str({True: 'TRUE', False: 'FALSE', None: 'None'}[value[0]])
        else:
            return str(value[0])

    def get_array_str(self, value):
        result = []
        for i in value[0].values():
            if i[1] == 'ARRAY':
                result.append(str(self.get_array_str(i)))
            else:
                result.append(self.get_str(i))
        return '[' + ', '.join(result) + ']'

    def exe(self):
        result = ''
        for i in self.expressions:
            t = i.exe()
            if t[1] == 'ARRAY':
                result += self.get_array_str(t)
            else:
                result += self.get_str(t)
        return result

class Input(AST_Node):
    def __init__(self, id, *args, **kwargs):
        self.type = 'INPUT'
        self.id = id
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id)

    def exe(self):
        stack.set_variable(self.id, str(input()), 'STRING')

class Array_input(AST_Node):
    def __init__(self, id, indexes, *args, **kwargs):
        self.type = 'ARRAY_INPUT'
        self.id = id
        self.indexes = indexes
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + self.indexes.get_tree(level+1)

    def exe(self):
        indexes = self.indexes.exe()
        target_id = self.id
        for index in indexes:
            target_id += '.' + str(index)
        stack.set_variable(target_id, str(input()), 'STRING')
