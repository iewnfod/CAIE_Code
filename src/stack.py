from .global_var import *
from .data_types import *

class Stack:
    def __init__(self) -> None:
        self.spaces = [('GLOBAL', {}, {})]  # [(空间名, {变量名: (类实例, 是否是常量)}, {函数名: 函数AST实例})]
        self.files = {}  # {文件名: 打开的文件实例}
        self.structs = {
            'INTEGER' : INTEGER,
            'REAL' : REAL,
            'STRING' : STRING,
            'CHAR' : CHAR,
            'BOOLEAN' : BOOLEAN,
            'ARRAY' : ARRAY,
        }  # {结构名: 结构实例}
        self.return_variables = None
        self.return_request = False

    def global_space(self):
        return self.spaces[-1]

    def current_space(self):
        return self.spaces[0]

    def get_variable(self, id):
        for i in self.spaces:
            if id in i[1].keys():
                return i[1][id][0]
        else:
            print(f'Stack Error: No variable or constant have id: `{id}`. ')

    def new_variable(self, id, type):
        self.spaces[0][1][id] = (self.structs[type](), False)

    def new_constant(self, id, type, value):
        self.spaces[0][1][id] = (self.structs[type](value), True)

    def set_variable(self, id, value, type):
        for i in range(len(self.spaces)):
            if id in self.spaces[i][1]:
                if self.spaces[i][1][id][1] == False:
                    try:
                        self.spaces[i][1][id][0].set_value(value)
                    except:
                        print(f'Stack Error: Cannot assign `{type}` to `{self.spaces[i][1][id][0][1]}`. ')
                else:
                    print(f'Stack Error: Cannot assign value of constant `{id}`. ')
                # 如果找到了这个变量存在，不管什么错误，都退出
                break
        else:
            print(f'Stack Error: Variable `{id}` has not been declared yet. ')

    def pop_space(self):
        self.spaces.pop(0)
        self.return_request = False

    def new_space(self, space_name, var_dict, func_dict):
        self.spaces.insert(0, (space_name, var_dict, func_dict))

    def set_return_variables(self, variables):
        self.return_variables = variables

    def get_return_variables(self):
        v = self.return_variables
        self.return_variables = None
        return v

    def add_function(self, function):
        self.current_space()[2][function.id] = function

    def get_function(self, id):
        for i in range(len(self.spaces)):
            if id in self.spaces[i][2].keys():
                return self.spaces[i][2][id]
        else:
            print(f'Stack Error: No function with id: `{id}`. ')

    def add_file(self, path, file_obj):
        try:
            file_obj.seek(0, 2)
            eof = file_obj.tell()
        except:
            eof = ''
        file_obj.seek(0)
        self.files[path] = (file_obj, eof)

    def get_file(self, path):
        if path in self.files:
            return self.files[path][0]
        else:
            print(f'Stack Error: File `{path}` has not opened. ')

    def get_eof(self, path):
        if path in self.files:
            return self.files[path][1]
        else:
            print(f'Stack Error: File `{path}` has not opened. ')

    def add_struct(self, id, obj):
        self.structs[id] = obj
