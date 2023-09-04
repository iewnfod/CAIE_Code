from .data import *
from ..AST_Base import *
from ..global_var import *
from ..data_types import DATE

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
        self.value = str(value).encode('raw_unicode_escape').decode('unicode_escape')
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

class Date(AST_Node):
    def __init__(self, value, *args, **kwargs):
        self.type = 'DATE'
        self.value = value
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + self.value

    def exe(self):
        return DATE(self.value)
