from src.AST.data import *
from src.AST_Base import *
from src.global_var import *

class Open_file(AST_Node):
    def __init__(self, file_path, file_mode, *args, **kwargs):
        self.type = 'OPENFILE'
        self.file_path = file_path
        self.file_mode = file_mode
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.file_path.get_tree(level+1) + '\n' + self.file_mode.get_tree(level+1)

    def exe(self):
        file_path = self.file_path.exe()
        if file_path[1] == 'STRING':
            if self.file_mode in {'READ', 'WRITE', 'APPEND', 'RANDOM'}:
                fm = {'READ': 'r', 'WRITE': 'w', 'APPEND': 'a', 'RANDOM': 'r'}[self.file_mode]
                f = open(file_path[0], fm)
                stack.add_file(file_path[0], f)
            else:
                add_error_message(f'Unknown file mode: `{self.file_mode}`. ', self)
        else:
            add_error_message(f'Expect `STRING` for a file path, but found `{file_path[1]}`. ', self)

class Close_file(AST_Node):
    def __init__(self, file_path, *args, **kwargs):
        self.type = 'CLOSEFILE'
        self.file_path = file_path
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.file_path.get_tree(level+1)

    def exe(self):
        file_path = self.file_path.exe()
        if file_path[1] == 'STRING':
            f = stack.get_file(file_path[0])
            f.close()
        else:
            add_error_message(f'Expect `STRING` for a file path, but found `{file_path[1]}`. ', self)

class Read_file(AST_Node):
    def __init__(self, file_path, id, *args, **kwargs):
        self.type = 'READFILE'
        self.file_path = file_path
        self.id = id
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.file_path.get_tree(level+1) + '\n' + LEVEL_STR * (level+1) + str(self.id)

    def exe(self):
        file_path = self.file_path.exe()
        if file_path[1] == 'STRING':
            f = stack.get_file(file_path[0])
            data = f.read().strip()
            stack.set_variable(self.id, data, 'STRING')
        else:
            add_error_message(f'Expect `STRING` for a file path, but found `{file_path[1]}`. ', self)

class Write_file(AST_Node):
    def __init__(self, file_path, value, *args, **kwargs):
        self.type = 'WRITEFILE'
        self.file_path = file_path
        self.value = value
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.file_path.get_tree(level+1) + '\n' + self.value.get_tree(level+1)

    def exe(self):
        file_path = self.file_path.exe()
        value = self.value.exe()
        if file_path[1] == 'STRING':
            f = stack.get_file(file_path[0])
            f.write(str(value[0]))
        else:
            add_error_message(f'Expect `STRING` for a file path, but found `{file_path[1]}`. ', self)
