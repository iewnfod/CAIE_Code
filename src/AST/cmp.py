from .data import *
from ..AST_Base import *
from ..global_var import *


class Cmp_less(AST_Node):
    def __init__(self, left, right, *args, **kwargs):
        self.type = 'LESS'
        self.left = left
        self.right = right
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level + 1) + '\n' + self.right.get_tree(
            level + 1)

    def exe(self):
        return self.left.exe()[0] < self.right.exe()[0], 'BOOLEAN'


class Cmp_greater(AST_Node):
    def __init__(self, left, right, *args, **kwargs):
        self.type = 'GREATER'
        self.left = left
        self.right = right
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level + 1) + '\n' + self.right.get_tree(
            level + 1)

    def exe(self):
        return self.left.exe()[0] > self.right.exe()[0], 'BOOLEAN'


class Cmp_less_equal(AST_Node):
    def __init__(self, left, right, *args, **kwargs):
        self.type = 'LESS_EQUAL'
        self.left = left
        self.right = right
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level + 1) + '\n' + self.right.get_tree(
            level + 1)

    def exe(self):
        return self.left.exe()[0] <= self.right.exe()[0], 'BOOLEAN'


class Cmp_greater_equal(AST_Node):
    def __init__(self, left, right, *args, **kwargs):
        self.type = 'GREATER_EQUAL'
        self.left = left
        self.right = right
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level + 1) + '\n' + self.right.get_tree(
            level + 1)

    def exe(self):
        return self.left.exe()[0] >= self.right.exe()[0], 'BOOLEAN'


class Cmp_equal(AST_Node):
    def __init__(self, left, right, *args, **kwargs):
        self.type = 'EQUAL'
        self.left = left
        self.right = right
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level + 1) + '\n' + self.right.get_tree(
            level + 1)

    def exe(self):
        return self.left.exe()[0] == self.right.exe()[0], 'BOOLEAN'


class Cmp_not_equal(AST_Node):
    def __init__(self, left, right, *args, **kwargs):
        self.type = 'NOT_EQUAL'
        self.left = left
        self.right = right
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level + 1) + '\n' + self.right.get_tree(
            level + 1)

    def exe(self):
        return self.left.exe()[0] != self.right.exe()[0], 'BOOLEAN'
