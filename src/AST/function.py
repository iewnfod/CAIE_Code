from .data import *
from ..AST_Base import *
from ..global_var import *
import copy

class Function(AST_Node):
    def __init__(self, id, parameters, statements, returns=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'FUNCTION'
        self.id = id
        self.parameters = parameters
        self.statements = statements
        self.returns = returns
        self.arr_type = None

    def get_tree(self, level=0):
        if self.parameters:
            return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + self.parameters.get_tree(level+1) + '\n' + self.statements.get_tree(level+1)
        else:
            return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + self.statements.get_tree(level+1)

    def exe(self):
        stack.add_function(self)

class ArrFunction(AST_Node):
    def __init__(self, id, parameters, arr_type, statements, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'FUNCTION'
        self.id = id
        self.parameters = parameters
        self.statements = statements
        self.returns = 'ARRAY'
        self.arr_type = arr_type

    def get_tree(self, level=0):
        if self.parameters:
            return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + self.parameters.get_tree(level+1) + '\n' + self.statements.get_tree(level+1)
        else:
            return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + self.statements.get_tree(level+1)

    def exe(self):
        stack.add_function(self)

class Call_function(AST_Node):
    def __init__(self, id, parameters=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'CALL_FUNCTION'
        self.id = id
        self.parameters = parameters

    def get_tree(self, level=0):
        if self.parameters:
            return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + self.parameters.get_tree(level+1)
        else:
            return LEVEL_STR * level + self.type + ' ' + str(self.id)

    def exe(self):
        new_dict = {}  # {变量名: (值, 类型, 是否是常量)}
        function_obj = stack.get_function(self.id)
        if function_obj.parameters:
            target_parameters = function_obj.parameters.exe()  # (id, 类型)
            if self.parameters:
                parameters = self.parameters.exe()  # (值, 类型)
            else:
                add_error_message(f'Function `{self.id}` expect {len(target_parameters)} parameters, but found 0', self)
            if len(target_parameters) != len(parameters):
                add_error_message(f'Function `{self.id}` expect {len(target_parameters)} parameters, but found {len(self.parameters)}', self)

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
                        # 切换 target 类型
                        if target_parameters[i][1] == 'ARRAY' and target_parameters[i][3]:
                            cp = copy.copy(parameters[i])
                            cp.to_target(target_parameters[i][3])
                            new_dict[target_parameters[i][0]] = (cp, False)
                        else:
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
                add_error_message(f'Function `{self.id}` does not expect any parameters, but found {len(self.parameters)}', self)

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
            if function_obj.returns == returns[1] and function_obj.returns == 'ARRAY':
                if function_obj.arr_type:
                    # 切换返回值的类型
                    returns.to_target(function_obj.arr_type)
                return returns
            # 查看返回值类型是否相同
            # 如果一样，就直接返回
            if function_obj.returns == returns[1]:
                return returns
            # 否则尝试创建对象进行返回
            try:
                return stack.structs[function_obj.returns](returns[0])
            except:
                add_error_message(f'Function {self.id} expect `{function_obj.returns}` to return, but found `{returns[1]}`', self)
        else:
            return None

class Declare_parameter(AST_Node):
    def __init__(self, id, type, by_ref=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'DECLARE_PARAMETER'
        self.id = id
        self.var_type = type
        self.by_ref = by_ref

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + LEVEL_STR * (level+1) + str(self.var_type)

    def exe(self):
        return (self.id, self.var_type, self.by_ref, None)

class Declare_arr_parameter(AST_Node):
    def __init__(self, id, arr_type, by_ref=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'DECLARE_ARR_PARAMETER'
        self.id = id
        self.var_type = 'ARRAY'
        self.arr_type = arr_type
        self.by_ref = by_ref

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + LEVEL_STR * (level + 1) + str(self.var_type) + ' ' + str(self.arr_type)

    def exe(self):
        return (self.id, self.var_type, self.by_ref, self.arr_type)

class Declare_parameters(AST_Node):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'DECLARE_PARAMETERS'
        self.parameters = []

    def get_tree(self, level=0):
        result = LEVEL_STR * level + self.type + '\n'
        for i in self.parameters:
            result += i.get_tree(level+1) + '\n'
        return result[:-1]

    def add_parameter(self, parameter):
        self.parameters.append(parameter)

    def __len__(self):
        return len(self.parameters)

    def exe(self):
        result = []
        for i in self.parameters:
            v = i.exe()
            if v[2] == None:
                if len(result):
                    v = (v[0], v[1], result[-1][2], v[3])
                else:
                    v = (v[0], v[1], False, v[3])
            result.append(v)
        return result

class Parameters(AST_Node):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'PARAMETERS'
        self.parameters = []

    def get_tree(self, level=0):
        result = LEVEL_STR * level + self.type + '\n'
        for i in self.parameters:
            result += i.get_tree(level+1) + '\n'
        return result[:-1]

    def add_parameter(self, parameter):
        self.parameters.append(parameter)

    def __len__(self):
        return len(self.parameters)

    def exe(self):
        result = []
        for i in self.parameters:
            result.append(i.exe())
        return result

class Return(AST_Node):
    def __init__(self, expression, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'RETURN'
        self.expression = expression

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        stack.set_return_variables(self.expression.exe())
        stack.return_request = True
