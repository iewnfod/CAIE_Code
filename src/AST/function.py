from src.AST.data import *
from src.AST_Base import *
from src.global_var import *
import copy

class Function(AST_Node):
    def __init__(self, id, parameters, statements, returns=None, *args, **kwargs):
        self.type = 'FUNCTION'
        self.id = id
        self.parameters = parameters
        self.statements = statements
        self.returns = returns
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + self.parameters.get_tree(level+1) + '\n' + self.statements.get_tree(level+1)

    def exe(self):
        stack.add_function(self)

class Call_function(AST_Node):
    def __init__(self, id, parameters=None, *args, **kwargs):
        self.type = 'CALL_FUNCTION'
        self.id = id
        self.parameters = parameters
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        new_dict = {}  # {变量名: (值, 类型, 是否是常量)}
        function_obj = stack.get_function(self.id)
        if function_obj.parameters:
            target_parameters = function_obj.parameters.exe()  # (id, 类型)
            parameters = self.parameters.exe()  # (值, 类型)
            if len(target_parameters) != len(parameters):
                add_error_message(f'Function `{self.id}` has wrong number of parameters', self)

            # 核对并传参
            for i in range(len(target_parameters)):
                try:
                    # 如果是要 by ref，那就直接传递类型实例
                    if target_parameters[i][2]:
                        if target_parameters[i][1] == parameters[i][1]:
                            new_dict[target_parameters[i][0]] = (parameters[i], False)
                        else:
                            add_error_message(f'Cannot reference `{parameters[i][1]}` to `{target_parameters[i][1]}`', self)
                    else:
                        # 否则，赋值 value 并且然后传递
                        new_dict[target_parameters[i][0]] = (
                            stack.structs[target_parameters[i][1]](
                                copy.copy(parameters[i][0])
                            ),
                            False
                        )
                except:
                    add_error_message(f'Function `{self.id}` expect a parameter with type `{target_parameters[i][1]}`, but found `{parameters[i][1]}`', self)
        else:
            if self.parameters:
                add_error_message(f'Function `{self.id}` does not expect any parameters, but found', self)

        # 为函数创建新的命名空间
        stack.new_space(self.id, new_dict, {})

        # 运行函数
        function_obj.statements.exe()
        # 获取返回值
        returns = stack.get_return_variables()

        # 删除命名空间
        stack.pop_space()

        # 核查返回值，并返回
        if function_obj.returns:
            # 查看返回值类型是否相同
            try:
                return stack.structs[function_obj.returns](returns[0])
            except:
                add_error_message(f'Function {self.id} expect `{function_obj.returns}` to return, but found `{returns[1]}`', self)
        else:
            return None

class Declare_parameter(AST_Node):
    def __init__(self, id, type, by_ref=None, *args, **kwargs):
        self.type = 'DECLARE_PARAMETER'
        self.id = id
        self.var_type = type
        self.by_ref = by_ref
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + LEVEL_STR * (level+1) + str(self.var_type)

    def exe(self):
        return (self.id, self.var_type, self.by_ref)

class Declare_parameters(AST_Node):
    def __init__(self, *args, **kwargs):
        self.type = 'DECLARE_PARAMETERS'
        self.parameters = []
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        result = LEVEL_STR * level + self.type + '\n'
        for i in self.parameters:
            result += i.get_tree(level+1) + '\n'
        return result[:-1]

    def add_parameter(self, parameter):
        self.parameters.append(parameter)

    def exe(self):
        result = []
        for i in self.parameters:
            v = i.exe()
            if v[2] == None:
                if len(result):
                    v = (v[0], v[1], result[-1][2])
                else:
                    v = (v[0], v[1], False)
            result.append(v)
        return result

class Parameters(AST_Node):
    def __init__(self, *args, **kwargs):
        self.type = 'PARAMETERS'
        self.parameters = []
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        result = LEVEL_STR * level + self.type + '\n'
        for i in self.parameters:
            result += i.get_tree(level+1) + '\n'
        return result[:-1]

    def add_parameter(self, parameter):
        self.parameters.append(parameter)

    def exe(self):
        result = []
        for i in self.parameters:
            result.append(i.exe())
        return result

class Return(AST_Node):
    def __init__(self, expression, *args, **kwargs):
        self.type = 'RETURN'
        self.expression = expression
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        stack.set_return_variables(self.expression.exe())
        stack.return_request = True
