from src.AST.data import *

class Logic_and:
    def __init__(self, left, right):
        self.type = 'AND'
        self.left = left
        self.right = right

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level+1) + '\n' + self.right.get_tree(level+1)

    def exe(self):
        return (self.left.exe()[0] and self.right.exe()[0], 'BOOLEAN')

class Logic_or:
    def __init__(self, left, right):
        self.type = 'OR'
        self.left = left
        self.right = right

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level+1) + '\n' + self.right.get_tree(level+1)

    def exe(self):
        return (self.left.exe()[0] or self.right.exe()[0], 'BOOLEAN')

class Logic_not:
    def __init__(self, value):
        self.type = 'NOT'
        self.value = value

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.value.get_tree(level+1)

    def exe(self):
        return (not self.value.exe()[0], 'BOOLEAN')
