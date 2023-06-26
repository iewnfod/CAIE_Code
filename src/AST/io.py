from src.AST.data import *

class Output:
    def __init__(self, value):
        self.type = 'OUTPUT'
        self.value = value

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.value.get_tree(level+1)

    def exe(self):
        print(self.value.exe()[0])

class Input:
    def __init__(self, id):
        self.type = 'INPUT'
        self.id = id

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id)

    def exe(self):
        stack.set_variable(self.id, input(), 'STRING')
