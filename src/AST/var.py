from .data import *
from ..AST_Base import *
from ..global_var import *

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
        stack.new_constant(self.id, value)

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

class Delete(AST_Node):
    def __init__(self, id, *args, **kwargs):
        self.type = 'DELETE'
        self.id = id
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id)

    def exe(self):
        stack.remove_variable(self.id)

class NewAssign(AST_Node):
    def __init__(self, target_expr, assign_expr, *args, **kwargs):
        self.type = 'NEW_ASSIGN'
        self.target_expr = target_expr
        self.assign_expr = assign_expr
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.target_expr.get_tree(level+1) + '\n' + self.assign_expr.get_tree(level+1)

    def exe(self):
        assign_item = self.assign_expr.exe()
        target_item = self.target_expr.exe()
        if target_item is not None:
            try:
                target_item.set_value(assign_item[0])
            except:
                add_error_message(f'Cannot assign `{assign_item}` to `{target_item}`', self)
        else:
            add_error_message(f'Target item does not exist', self)
