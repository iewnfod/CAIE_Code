from .data import *
from ..AST_Base import *
from ..global_var import *
from .array import *
from .data_types import *

class Open_file(AST_Node):
    def __init__(self, file_path, file_mode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'OPENFILE'
        self.file_path = file_path
        self.file_mode = file_mode

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.file_path.get_tree(level+1) + '\n' + self.file_mode.get_tree(level+1)

    def exe(self):
        file_path = self.file_path.exe()
        if file_path[1] == 'STRING':
            if self.file_mode in {'READ', 'WRITE', 'APPEND', 'RANDOM'}:
                fm = {'READ': 'r', 'WRITE': 'w', 'APPEND': 'a', 'RANDOM': 'w+'}[self.file_mode]
                f = open(file_path[0], fm)
                stack.add_file(file_path[0], f)
            else:
                add_error_message(f'Unknown file mode: `{self.file_mode}`', self)
        else:
            add_error_message(f'Expect `STRING` for a file path, but found `{file_path[1]}`', self)

class Close_file(AST_Node):
    def __init__(self, file_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'CLOSEFILE'
        self.file_path = file_path

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.file_path.get_tree(level+1)

    def exe(self):
        file_path = self.file_path.exe()
        if file_path[1] == 'STRING':
            f = stack.get_file(file_path[0])
            f.flush()
            f.close()
        else:
            add_error_message(f'Expect `STRING` for a file path, but found `{file_path[1]}`', self)

class Read_file(AST_Node):
    def __init__(self, file_path, id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'READFILE'
        self.file_path = file_path
        self.id = id

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.file_path.get_tree(level+1) + '\n' + LEVEL_STR * (level+1) + str(self.id)

    def exe(self):
        file_path = self.file_path.exe()
        if file_path[1] == 'STRING':
            f = stack.get_file(file_path[0])
            data = f.readline().strip()
            stack.set_variable(self.id, data, 'STRING')
        else:
            add_error_message(f'Expect `STRING` for a file path, but found `{file_path[1]}`', self)

class Read_file_array(AST_Node):
    def __init__(self, file_path, id, indexes, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'READFILE_ARRAY'
        self.file_path = file_path
        self.id = id
        self.indexes = indexes

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.file_path(level+1) + '\n' + LEVEL_STR * (level+1) + str(self.id) + '\n' + self.indexes.get_tree(level+1)

    def exe(self):
        fp = self.file_path.exe()
        if fp[1] == 'STRING' :
            f = stack.get_file(fp[0])
            data = f.read()
            Array_assign(
                self.id,
                self.indexes,
                String(data, lineno=self.lineno, lexpos=self.lexpos),
                lineno=self.lineno,
                lexpos=self.lexpos
            ).exe()
        else:
            add_error_message(f'Expect `STRING` for a file path, but found `{fp[1]}`', self)

class Write_file(AST_Node):
    def __init__(self, file_path, value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'WRITEFILE'
        self.file_path = file_path
        self.value = value

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.file_path.get_tree(level+1) + '\n' + self.value.get_tree(level+1)

    def exe(self):
        file_path = self.file_path.exe()
        value = self.value.exe()
        if file_path[1] == 'STRING':
            f = stack.get_file(file_path[0])
            f.write(str(value[0]))
            # f.flush()
        else:
            add_error_message(f'Expect `STRING` for a file path, but found `{file_path[1]}`', self)

class Seek(AST_Node):
    def __init__(self, file_path, ad, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'SEEK'
        self.file_path = file_path
        self.ad = ad

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.file_path.get_tree(level+1) + '\n' + self.ad.get_tree(level+1)

    def exe(self):
        fp = self.file_path.exe()
        ad = self.ad.exe()
        if fp[1] == 'STRING':
            if self.ad[1] == 'INTEGER':
                f = stack.get_file(fp[0])
                f.seek(ad[0], 0)
            else:
                add_error_message(f'Expect `INTEGER` for a address, but found `{ad[1]}`', self)
        else:
            add_error_message(f'Expect `STRING` for a file path, but found `{fp[1]}`', self)
