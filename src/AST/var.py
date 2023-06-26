from src.AST.data import *

class Constant:
    def __init__(self, id, value):
        self.type = 'CONSTANT'
        self.id = id
        self.value = value

    def get_tree(self, level=0):
        result = LEVEL_STR * level + self.type + '\n' + str(self.id) + '\n' + str(self.value)
        return result

    def exe(self):
        value = self.value.exe()
        stack.new_constant(self.id, value[1], value[0])

class Variable:
    def __init__(self, id, type):
        self.type = 'VARIABLE'
        self.id = id
        self.var_type = type

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + str(self.id) + '\n' + str(self.var_type)

    def exe(self):
        stack.new_variable(self.id, self.var_type)

class Assign:
    def __init__(self, id, expression):
        self.type = 'ASSIGN'
        self.id = id
        self.expression = expression

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + LEVEL_STR * (level + 1) + str(self.id) + '\n' + self.expression.get_tree(level + 1)

    def exe(self):
        r = self.expression.exe()
        stack.set_variable(self.id, r[0], r[1])

# 唯一获取变量及常量值的方法
class Get:
    def __init__(self, id):
        self.type = 'GET'
        self.id = id

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id)

    def exe(self):
        return stack.get_variable(self.id)
