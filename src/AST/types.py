from .data import *
from ..AST_Base import *
from ..global_var import *
from .var import *
from .array import *
from ..stack import Space


class Enumerate_type(AST_Node):
    def __init__(self, id, enumerate_items, *args, **kwargs):
        self.type = "ENUMERATE_TYPE"
        self.id = id
        self.items = enumerate_items
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + LEVEL_STR * (level + 1) + str(
            self.id) + '\n' + self.items.get_tree(level + 1)

    def exe(self):
        items = self.items.exe()
        stack.new_variable(self.id, 'ENUM')
        stack.set_variable(self.id, items, 'ENUM')


class Enumerate_items(AST_Node):
    def __init__(self, *args, **kwargs):
        self.type = 'ENUMERATE_ITEMS'
        self.items = []
        super().__init__(*args, **kwargs)

    def add_item(self, id):
        self.items.append(id)

    def get_tree(self, level=0):
        result = LEVEL_STR * level + self.type
        for i in self.items:
            result += '\n' + LEVEL_STR * (level + 1) + str(i)
        return result

    def exe(self):
        return self.items


class Composite_type(AST_Node):
    def __init__(self, id, body_expression, *args, **kwargs):
        self.type = 'COMPOSITE_TYPE'
        self.id = id
        self.body = body_expression
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + LEVEL_STR * (level + 1) + str(
            self.id) + '\n' + self.body.get_tree(level + 1)

    def exe(self):
        that = self

        class t:
            def __init__(self, name):
                self.name = name
                self.type = that.id
                self.body = that.body
                self.is_struct = True
                self.space = Space(self.type, {}, {})
                stack.push_subspace(self.space)
                self.body.exe()
                stack.pop_subspace()

            def __getitem__(self, i):
                if i == 1:
                    return self.type
                else:
                    return self

            def __str__(self):
                space = self.space
                s = self.type
                if space.variables:
                    str_variables = {}
                    for key, value in space.variables.items():
                        str_variables[str(key)] = str(value[0])
                    s += f' {str_variables}'
                if space.functions:
                    str_functions = {}
                    for key, value in space.functions.items():
                        str_functions[str(key)] = str(value)
                    s += f' {str_functions}'
                return s

            def set_value(self, value):
                # 将对方的 subspace 设置为自己的
                if value.type == self.type:
                    self.space = value.space
                else:
                    add_stack_error_message(f'Cannot assign `{value.type}` to `{self.type}`')

        stack.add_struct(self.id, t)


class Composite_type_expression(AST_Node):
    def __init__(self, exp1, exp2, *args, **kwargs):
        self.type = 'COMPOSITE_TYPE_EXPRESSION'
        self.exp1 = exp1
        self.exp2 = exp2
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.exp1.get_tree(level + 1) + '\n' + self.exp2.get_tree(
            level + 2)

    def exe(self):
        obj = self.exp1.exe()[0]
        # 判断一下是不是枚举类型
        if obj[1] == 'ENUM':
            return (obj[0].__members__[self.id], 'ENUM')
        # 否则，按照正常自定义类型的操作运行
        # 将此对象的空间放入主空间列表
        stack.push_subspace(obj.space)
        # 获取变量的值
        v = self.exp2.exe()
        # 将空间放回子空间列表
        stack.pop_subspace()
        # 返回获得的值
        return v


class Composite_type_statement(AST_Node):
    def __init__(self, exp, statement, *args, **kwargs):
        self.type = 'COMPOSITE_TYPE_STATEMENT'
        self.exp = exp
        self.statement = statement
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.exp.get_tree(level + 1) + '\n' + self.statement.get_tree(
            level + 2)

    def exe(self):
        obj = self.exp.exe()
        # 判断一下是不是枚举类型
        if obj[1] == 'ENUM':
            return (obj[0].__members__[self.id], 'ENUM')
        # 否则，按照正常自定义类型的操作运行
        # 将此对象的空间放入主空间列表
        stack.push_subspace(obj.space)
        # 获取变量的值
        self.statement.exe()
        # 将空间放回子空间列表
        stack.pop_subspace()


class Pointer(AST_Node):
    def __init__(self, new_id, old_id, *args, **kwargs):
        self.type = 'POINTER'
        self.new_id = new_id
        self.old_id = old_id
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + LEVEL_STR * (level + 1) + str(self.new_id) + '\n' + LEVEL_STR * (
                    level + 1) + str(self.old_id)

    def exe(self):
        stack.add_struct(self.new_id, stack.structs[self.old_id])
