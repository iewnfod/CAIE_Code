from src.AST.data import *

class Cmp_less:
    def __init__(self, left, right):
        self.type = 'LESS'
        self.left = left
        self.right = right

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level+1) + '\n' + self.right.get_tree(level+1)

    def exe(self):
        return (self.left.exe()[0] < self.right.exe()[0], 'BOOLEAN')

class Cmp_greater:
    def __init__(self, left, right):
        self.type = 'GREATER'
        self.left = left
        self.right = right

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level+1) + '\n' + self.right.get_tree(level+1)

    def exe(self):
        return (self.left.exe()[0] > self.right.exe()[0], 'BOOLEAN')

class Cmp_less_equal:
    def __init__(self, left, right):
        self.type = 'LESS_EQUAL'
        self.left = left
        self.right = right

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level+1) + '\n' + self.right.get_tree(level+1)

    def exe(self):
        return (self.left.exe()[0] <= self.right.exe()[0], 'BOOLEAN')

class Cmp_greater_equal:
    def __init__(self, left, right):
        self.type = 'GREATER_EQUAL'
        self.left = left
        self.right = right

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level+1) + '\n' + self.right.get_tree(level+1)

    def exe(self):
        return (self.left.exe()[0] >= self.right.exe()[0], 'BOOLEAN')

class Cmp_equal:
    def __init__(self, left, right):
        self.type = 'EQUAL'
        self.left = left
        self.right = right

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level+1) + '\n' + self.right.get_tree(level+1)

    def exe(self):
        return (self.left.exe()[0] == self.right.exe()[0], 'BOOLEAN')

class Cmp_not_equal:
    def __init__(self, left, right):
        self.type = 'NOT_EQUAL'
        self.left = left
        self.right = right

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level+1) + '\n' + self.right.get_tree(level+1)

    def exe(self):
        return (self.left.exe()[0] != self.right.exe()[0], 'BOOLEAN')
