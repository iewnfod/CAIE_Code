from src.AST.data import *

class Op_minus:
    def __init__(self, left, right):
        self.type = 'MINUS'
        self.left = left
        self.right = right

    def get_tree(self, level=0):
        return LEVEL_STR * self.level + self.type + '\n' + self.left.get_tree(level+1) + '\n' + self.right.get_tree(level+1)

    def exe(self):
        n1 = self.left.exe()
        n2 = self.right.exe()
        if n1[1] == n2[1]:
            return (n1[0] - n2[0], n1[1])
        elif n1[1] == 'INTEGER' and n2[1] == 'REAL' or n1[1] == 'REAL' and n2[1] == 'INTEGER':
            return (n1[0] - n2[0], 'REAL')
        else:
            print(f'Cannot minus `{n1[1]}` with `{n2[1]}`')

class Op_plus:
    def __init__(self, left, right):
        self.type = 'PLUS'
        self.left = left
        self.right = right

    def get_tree(self, level=0):
        return LEVEL_STR * self.level + self.type + '\n' + self.left.get_tree(level+1) + '\n' + self.right.get_tree(level+1)

    def exe(self):
        n1 = self.left.exe()
        n2 = self.right.exe()
        if n1[1] == n2[1]:
            return (n1[0] + n2[0], n1[1])
        elif n1[1] == 'INTEGER' and n2[1] == 'REAL' or n1[1] == 'REAL' and n2[1] == 'INTEGER':
            return (n1[0] + n2[0], 'REAL')
        else:
            print(f'Cannot plus `{n1[1]}` with `{n2[1]}`')

class Op_mul:
    def __init__(self, left, right):
        self.type = 'MUL'
        self.left = left
        self.right = right

    def get_tree(self, level=0):
        return LEVEL_STR * self.level + self.type + '\n' + self.left.get_tree(level+1) + '\n' + self.right.get_tree(level+1)

    def exe(self):
        n1 = self.left.exe()
        n2 = self.right.exe()
        if n1[1] == n2[1]:
            return (n1[0] * n2[0], 'REAL')
        else:
            print(f'Cannot multiply `{n1[1]}` with `{n2[1]}`')

class Op_div:
    def __init__(self, left, right):
        self.type = 'DIV'
        self.left = left
        self.right = right

    def get_tree(self, level=0):
        return LEVEL_STR * self.level + self.type + '\n' + self.left.get_tree(level+1) + '\n' + self.right.get_tree(level+1)

    def exe(self):
        n1 = self.left.exe()
        n2 = self.right.exe()
        if n1[1] == n2[1]:
            return (n1[0] / n2[0], 'REAL')
        else:
            print(f'Cannot divide `{n1[1]}` with `{n2[1]}`')
