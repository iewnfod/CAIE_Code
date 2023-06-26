from src.AST.data import *

class Op_minus:
    def __init__(self, left, right):
        self.type = 'MINUS'
        self.left = left
        self.right = right

    def get_tree(self, level=0):
        return LEVEL_STR * self.level + self.type + '\n' + self.left.get_tree(level+1) + '\n' + self.right.get_tree(level+1)

    def exe(self):
        return self.left.exe() - self.right.exe()

class Op_plus:
    def __init__(self, left, right):
        self.type = 'PLUS'
        self.left = left
        self.right = right

    def get_tree(self, level=0):
        return LEVEL_STR * self.level + self.type + '\n' + self.left.get_tree(level+1) + '\n' + self.right.get_tree(level+1)

    def exe(self):
        return self.left.exe() + self.right.exe()

class Op_mul:
    def __init__(self, left, right):
        self.type = 'MUL'
        self.left = left
        self.right = right

    def get_tree(self, level=0):
        return LEVEL_STR * self.level + self.type + '\n' + self.left.get_tree(level+1) + '\n' + self.right.get_tree(level+1)

    def exe(self):
        return self.left.exe() * self.right.exe()

class Op_div:
    def __init__(self, left, right):
        self.type = 'DIV'
        self.left = left
        self.right = right

    def get_tree(self, level=0):
        return LEVEL_STR * self.level + self.type + '\n' + self.left.get_tree(level+1) + '\n' + self.right.get_tree(level+1)

    def exe(self):
        return self.left.exe() / self.right.exe()
