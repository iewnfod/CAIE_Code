from src.AST.data import *

class Function:
    def __init__(self, id, parameters, statements, returns=None):
        self.type = 'FUNCTION'
        self.id = id
        self.parameters = parameters
        self.statements = statements
        self.returns = returns

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + self.parameters.get_tree(level+1) + '\n' + self.statements.get_tree(level+1)

    def exe(self):
        stack.add_function(self)

class Call_function:
    def __init__(self, id, parameters=None):
        self.type = 'CALL_FUNCTION'
        self.id = id
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        new_dict = {}  # {变量名: (值, 类型, 是否是常量)}
        function_obj = stack.get_function(self.id)
        if function_obj.parameters:
            target_parameters = function_obj.parameters.exe()  # (id, 类型)
            parameters = self.parameters.exe()  # (值, 类型)
            if len(target_parameters) != len(parameters):
                print(f'Function `{self.id}` has wrong number of parameters. ')

            # 核对并传参
            for i in range(len(target_parameters)):
                if target_parameters[i][1] == parameters[i][1]:
                    new_dict[target_parameters[i][0]] = (parameters[i][0], parameters[i][1], False)
                else:
                    print(f'Function `{self.id}` expect a parameter with type `{target_parameters[i][1]}`, but found `{parameters[i][1]}`')
        else:
            if self.parameters:
                print(f'Function `{self.id}` does not expect any parameters, but found. ')

        # 为函数创建新的命名空间
        stack.new_space(self.id, new_dict)

        # 运行函数
        function_obj.statements.exe()
        # 获取返回值
        returns = stack.get_return_variables()

        # 删除命名空间
        stack.pop_space()

        # 核查返回值，并返回
        if function_obj.returns:
            # 查看返回值类型是否相同
            if returns[1] == function_obj.returns:
                return returns
            else:
                print(f'Function {self.id} expect `{function_obj.returns}` to return, but found `{returns[1]}`')
        else:
            return None

class Declare_parameter:
    def __init__(self, id, type):
        self.type = 'DECLARE_PARAMETER'
        self.id = id
        self.var_type = type

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + LEVEL_STR * (level+1) + str(self.var_type)

    def exe(self):
        return (self.id, self.var_type)

class Declare_parameters:
    def __init__(self):
        self.type = 'DECLARE_PARAMETERS'
        self.parameters = []

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

class Parameters:
    def __init__(self):
        self.type = 'PARAMETERS'
        self.parameters = []

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

class Return:
    def __init__(self, expression):
        self.type = 'RETURN'
        self.expression = expression

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        stack.set_return_variables(self.expression.exe())
