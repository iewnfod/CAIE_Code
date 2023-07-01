from src.AST.data import *
from src.AST_Base import *
from src.global_var import *

class Constant(AST_Node):
    def __init__(self, id, value, *args, **kwargs):
        self.type = 'CONSTANT'
        self.id = id
        self.value = value
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        result = LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + self.value.get_tree(level+1)
        return result

    def exe(self):
        value = self.value.exe()
        stack.new_constant(self.id, value[1], value[0])

class Variable(AST_Node):
    def __init__(self, id, type, *args, **kwargs):
        self.type = 'VARIABLE'
        self.id = id
        self.var_type = type
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + LEVEL_STR * (level+1) + str(self.var_type)

    def exe(self):
        stack.new_variable(self.id, self.var_type)

class Assign(AST_Node):
    def __init__(self, id, expression, *args, **kwargs):
        self.type = 'ASSIGN'
        self.id = id
        self.expression = expression
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + self.expression.get_tree(level + 1)

    def exe(self):
        r = self.expression.exe()
        stack.set_variable(self.id, r[0], r[1])

# 唯一获取变量及常量值的方法
class Get(AST_Node):
    def __init__(self, id, *args, **kwargs):
        self.type = 'GET'
        self.id = id
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id)

    def exe(self):
        return stack.get_variable(self.id)
