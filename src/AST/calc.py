from .data import *
from ..AST_Base import *
from ..global_var import *


class Op_minus(AST_Node):
    def __init__(self, left, right, *args, **kwargs):
        self.type = 'MINUS'
        self.left = left
        self.right = right
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level + 1) + '\n' + self.right.get_tree(
            level + 1)

    def exe(self):
        n1 = self.left.exe()
        n2 = self.right.exe()
        try:
            v = n1[0] - n2[0]
            if int(v) == v:
                return (int(v), 'INTEGER')
            else:
                return (v, 'REAL')
        except:
            add_error_message(f'Cannot minus `{n1[1]}` with `{n2[1]}`', self)


class Op_plus(AST_Node):
    def __init__(self, left, right, *args, **kwargs):
        self.type = 'PLUS'
        self.left = left
        self.right = right
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level + 1) + '\n' + self.right.get_tree(
            level + 1)

    def exe(self):
        n1 = self.left.exe()
        n2 = self.right.exe()
        try:
            v = n1[0] + n2[0]
            if int(v) == v:
                return (int(v), 'INTEGER')
            else:
                return (v, 'REAL')
        except:
            add_error_message(f'Cannot plus `{n1[1]}` with `{n2[1]}`', self)


class Op_mul(AST_Node):
    def __init__(self, left, right, *args, **kwargs):
        self.type = 'MUL'
        self.left = left
        self.right = right
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level + 1) + '\n' + self.right.get_tree(
            level + 1)

    def exe(self):
        n1 = self.left.exe()
        n2 = self.right.exe()
        try:
            v = n1[0] * n2[0]
            if int(v) == v:
                return (int(v), 'INTEGER')
            else:
                return (v, 'REAL')
        except:
            add_error_message(f'Cannot multiply `{n1[1]}` with `{n2[1]}`', self)


class Op_div(AST_Node):
    def __init__(self, left, right, *args, **kwargs):
        self.type = 'DIV'
        self.left = left
        self.right = right
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level + 1) + '\n' + self.right.get_tree(
            level + 1)

    def exe(self):
        n1 = self.left.exe()
        n2 = self.right.exe()
        try:
            # 检查除数是否是 0
            if n2[0] == 0:
                add_error_message('Cannot divide by zero', self)
                return (0, 'INTEGER')

            v = n1[0] / n2[0]
            if int(v) == v:
                return (int(v), 'INTEGER')
            else:
                return (v, 'REAL')
        except:
            add_error_message(f'Cannot divide `{n1[1]}` with `{n2[1]}`', self)


class Op_connect(AST_Node):
    def __init__(self, left, right, *args, **kwargs):
        self.type = 'CONNECT'
        self.left = left
        self.right = right
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level + 1) + '\n' + self.right.get_tree(
            level + 1)

    def exe(self):
        s1 = self.left.exe()
        s2 = self.right.exe()
        try:
            return (s1[0] + s2[0], 'STRING')
        except:
            add_error_message(f'Cannot connect `{s1[1]}` with `{s2[1]}`', self)


class Op_mod(AST_Node):
    def __init__(self, left, right, *args, **kwargs):
        self.type = 'MOD'
        self.left = left
        self.right = right
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level + 1) + '\n' + self.right.get_tree(
            level + 1)

    def exe(self):
        n1 = self.left.exe()
        n2 = self.right.exe()
        try:
            v = n1[0] % n2[0]
            if int(v) == v:
                return (int(v), 'INTEGER')
            else:
                return (v, 'REAL')
        except:
            add_error_message(f'Cannot module `{n1[1]}` with `{n2[1]}`', self)


class Op_exact_div(AST_Node):
    def __init__(self, left, right, *args, **kwargs):
        self.type = 'EXACT_DIV'
        self.left = left
        self.right = right
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.left.get_tree(level + 1) + '\n' + self.right.get_tree(
            level + 1)

    def exe(self):
        n1 = self.left.exe()
        n2 = self.right.exe()
        try:
            v = n1[0] // n2[0]
            return (int(v), 'INTEGER')
        except:
            add_error_message(f'Cannot exact divide `{n1[1]}` with `{n2[1]}`', self)
