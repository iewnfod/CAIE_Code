from .global_var import *
from .data_types import *
from .history import HOME_PATH
from copy import copy

# (空间名, {变量名: (类实例, 是否是常量)}, {函数名: 函数AST实例})
class Space:
    def __init__(self, name: str, variables: dict, functions: dict):
        self.name = name
        self.variables = variables
        self.functions = functions

    def __getitem__(self, index):
        if index == 0:
            return self.name
        elif index == 1:
            return self.variables
        elif index == 2:
            return self.functions
        else:
            raise IndexError(f'Invalid index `{index}` for space `{self.name}`')

    def new_variable(self, id, value, is_const):
        self.variables[id] = (value, is_const)

    def set_variable(self, id, value, type):
        if self.variables[id][1] == False:
            try:
                self.variables[id][0].set_value(value)
            except:
                add_stack_error_message(f'Cannot assign `{type}` to `{self.variables[id][0][1]}`')
        else:
            add_stack_error_message(f'Cannot assign value to constant `{id}`')

    def force_set_variable(self, id, value, type):
        if self.variables[id][1] == False:
            if self.variables[id][0][1] == type:
                self.variables[id] = (value, False)
            else:
                add_stack_error_message(f'Cannot assign `{type}` pointer to `{self.variables[id][0][1]}`')
        else:
            add_stack_error_message(f'Cannot assign value to constant `{id}`')

    def set_function(self, id, func):
        self.functions[id] = func


class Stack:
    def __init__(self) -> None:
        self.spaces = [Space('GLOBAL', {}, {})]  # [Space]
        self.files = {}  # {文件名: 打开的文件实例}
        self.structs = {
            'INTEGER' : INTEGER,
            'REAL' : REAL,
            'STRING' : STRING,
            'CHAR' : CHAR,
            'BOOLEAN' : BOOLEAN,
            'DATE': DATE,
            'ARRAY' : ARRAY,
            'ENUM' : ENUM,
            'ANY': ANY,
        }  # {结构名: 结构实例}
        self.return_variables = None
        self.return_request = False
        # 内置常量
        self.new_constant('__HOME__', STRING(HOME_PATH))

    def global_space(self):
        return self.spaces[-1]

    def current_space(self):
        return self.spaces[0]

    def get_variable(self, id):
        for i in self.spaces:
            if id in i.variables.keys():
                v = i.variables[id][0]
                if v.current_space is None: return v
                else:
                    # 判断是否是在外部访问
                    # 从后向前遍历，如果这个变量中记录的space存在于我的上面的话，那就可以
                    for i in range(len(self.spaces)-2, 0, -1):
                        if self.spaces[i] == v.current_space:
                            return v
                    else:
                        add_stack_error_message(f'Private variable `{id}` is not accessible')
        else:
            add_stack_error_message(f'No variable or constant have id: `{id}`')

    def new_variable(self, id, type, value=None):
        if value:
            self.spaces[0].new_variable(id, self.structs[type](name=id, value=value), False)
        else:
            self.spaces[0].new_variable(id, self.structs[type](name=id), False)

    def new_constant(self, id, value):
        # 复制值
        if type(value) == tuple:
            clone = self.structs[value[1]](value[0])
        else:
            clone = copy(value)
        # 赋值
        clone.is_const = True
        self.spaces[0].new_variable(id, clone, True)

    def set_variable(self, id, value, type):
        for i in range(len(self.spaces)):
            if id in self.spaces[i].variables:
                self.spaces[i].set_variable(id, value, type)
                break
        else:
            add_stack_error_message(f'Variable `{id}` has not been declared yet')

    def force_set_variable(self, id, value, type):
        for i in range(len(self.spaces)):
            if id in self.spaces[i].variables:
                self.spaces[i].force_set_variable(id, value, type)
                break
        else:
            add_stack_error_message(f'Variable `{id}` has not been declared yet')

    def remove_variable(self, id):
        for i in range(len(self.spaces)):
            if id in self.spaces[i].variables:
                del self.spaces[i].variables[id]
                return
        else:
            add_stack_error_message(f'Variable or constant `{id}` has not been declared yet')

    def pop_space(self):
        self.spaces.pop(0)
        self.return_request = False

    def new_space(self, space_name, var_dict, func_dict):
        self.spaces.insert(0, Space(space_name, var_dict, func_dict))

    def set_return_variables(self, variables):
        self.return_variables = variables

    def get_return_variables(self):
        v = self.return_variables
        self.return_variables = None
        return v

    def add_function(self, function):
        self.current_space().set_function(function.id, function)

    def get_function(self, id):
        for i in range(len(self.spaces)):
            if id in self.spaces[i].functions.keys():
                f = self.spaces[i].functions[id]
                if f.current_space is None: return f
                else:
                    # 与获取变量同理
                    for i in range(len(self.spaces)-2, 0, -1):
                        if self.spaces[i] == f.current_space:
                            return f
                    else:
                        add_stack_error_message(f'Private function `{id}` is not accessible')
        else:
            add_stack_error_message(f'No function with id: `{id}`')

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
            add_stack_error_message(f'File `{path}` has not opened')

    def get_eof(self, path):
        if path in self.files:
            return self.files[path][1]
        else:
            add_stack_error_message(f'File `{path}` has not opened')

    def close_all_files(self):
        for path, f in self.files.items():
            add_stack_error_message(f'Program exit before closing file `{path}`')
            f[0].close()

    def add_struct(self, id, obj):
        self.structs[id] = obj

    def pop_subspace(self):
        self.spaces.pop(0)

    def push_subspace(self, space):
        self.spaces.insert(0, space)

    def delete(self):
        del self
