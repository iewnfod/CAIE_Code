from .data import *
from ..AST_Base import *
from ..global_var import *
from enum import Enum

class Enumerate_type(AST_Node):
    def __init__(self, id, enumerate_items, *args, **kwargs):
        self.type = "ENUMERATE_TYPE"
        self.id = id
        self.items = enumerate_items
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + LEVEL_STR * (level+1) + str(self.id) + '\n' + self.items.get_tree(level+1)

    def exe(self):
        items = self.items.exe()
        obj = Enum(self.id, items)
        stack.add_struct(self.id, obj)

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
            result += '\n' + LEVEL_STR * (level+1) + str(i)
        return result

    def exe(self):
        return self.items

class Enumerate_get(AST_Node):
    def __init__(self, id, item, *args, **kwargs):
        self.type = 'ENUMERATE_GET'
        self.id = id
        self.item = item

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + LEVEL_STR * (level + 1) + str(self.id) + '\n' + LEVEL_STR * (level + 1) + str(self.item)

    def exe(self):
        obj = stack.structs[self.id]
        return (obj.__members__[self.item], self.id)
