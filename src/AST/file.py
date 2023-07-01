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
        file_mode = self.file_mode.exe()
