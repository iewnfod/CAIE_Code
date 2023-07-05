from src.AST.data import *
from src.AST_Base import *
from src.global_var import *

class Integer(AST_Node):
    def __init__(self, value, *args, **kwargs):
        self.type = 'INTEGER'
        self.value = value
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.value)

    def exe(self):
        return (self.value, self.type)

class Real(AST_Node):
    def __init__(self, value, *args, **kwargs):
        self.type = 'REAL'
        self.value = value
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.value)

    def exe(self):
        return (self.value, self.type)

class Char(AST_Node):
    def __init__(self, value, *args, **kwargs):
        self.type = 'CHAR'
        self.value = str(value)
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + "'" + str(self.value) + "'"

    def exe(self):
        return (self.value, self.type)

class String(AST_Node):
    def __init__(self, value, *args, **kwargs):
        self.type = 'STRING'
        self.value = str(value).encode('utf8').decode('unicode_escape')
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + '"' + str(self.value) + '"'

    def exe(self):
        return (self.value, self.type)

class Boolean(AST_Node):
    def __init__(self, value, *args, **kwargs):
        self.type = 'BOOLEAN'
        self.value = value
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.value)

    def exe(self):
        return (self.value, self.type)
