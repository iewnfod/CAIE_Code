from .data import *
from ..AST_Base import *
from ..global_var import *


class Logic_and(AST_Node):
    def __init__(self, left, right, *args, **kwargs):
        self.type = 'AND'
        self.left = left
        self.right = right
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level + 1) + '\n' + self.right.get_tree(
            level + 1)

    def exe(self):
        return (bool(self.left.exe()[0] and self.right.exe()[0]), 'BOOLEAN')


class Logic_or(AST_Node):
    def __init__(self, left, right, *args, **kwargs):
        self.type = 'OR'
        self.left = left
        self.right = right
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level + 1) + '\n' + self.right.get_tree(
            level + 1)

    def exe(self):
        return (bool(self.left.exe()[0] or self.right.exe()[0]), 'BOOLEAN')


class Logic_not(AST_Node):
    def __init__(self, value, *args, **kwargs):
        self.type = 'NOT'
        self.value = value
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.value.get_tree(level + 1)

    def exe(self):
        return (bool(not self.value.exe()[0]), 'BOOLEAN')
