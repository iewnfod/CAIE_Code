from src.AST.data import *

class Integer:
    def __init__(self, value):
        self.type = 'INTEGER'
        self.value = value

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.value)

    def exe(self):
        return (self.value, self.type)

class Real:
    def __init__(self, value):
        self.type = 'REAL'
        self.value = value

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.value)

    def exe(self):
        return (self.value, self.type)

class Char:
    def __init__(self, value):
        self.type = 'CHAR'
        self.value = value

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.value)

    def exe(self):
        return (self.value, self.type)

class String:
    def __init__(self, value):
        self.type = 'STRING'
        self.value = value

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.value)

    def exe(self):
        return (self.value, self.type)

class Boolean:
    def __init__(self, value):
        self.type = 'BOOLEAN'
        self.value = value

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.value)

    def exe(self):
        return (self.value, self.type)
