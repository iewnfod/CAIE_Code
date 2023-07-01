from src.AST.data import *
from random import randint
from src.AST_Base import *
from src.global_var import *

class Int_convert(AST_Node):
    def __init__(self, expression, *args, **kwargs):
        self.type = 'INTEGER_CONVERT'
        self.expression = expression
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        result = self.expression.exe()
        if len(result) != 1:
            add_error_message(f'`{self.type}` could only convert one parameter.', self)
            return
        else:
            result = result[0]
        try:
            result = int(result[0])
            return (result, 'INTEGER')
        except:
            add_error_message(f'Cannot convert `{result[0]}` into `INTEGER`', self)

class Str_convert(AST_Node):
    def __init__(self, expression, *args, **kwargs):
        self.type = 'STRING_CONVERT'
        self.expression = expression
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        result = self.expression.exe()
        if len(result) != 1:
            add_error_message(f'`{self.type}` could only convert one parameter.', self)
            return
        else:
            result = result[0]
        try:
            result = str(result[0])
            return (result, 'STRING')
        except:
            add_error_message(f'Cannot convert `{result[0]}` into `STRING`', self)

class Char_convert(AST_Node):
    def __init__(self, expression, *args, **kwargs):
        self.type = 'CHAR_CONVERT'
        self.expression = expression
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        result = self.expression.exe()
        if len(result) != 1:
            add_error_message(f'`{self.type}` could only convert one parameter. ', self)
            return
        else:
            result = result[0]


        try:
            result = str(result[0])
        except:
            add_error_message(f'Cannot convert `{result[0]}` into `CHAR`. ', self)
            return

        # 判断长度，如果不是1，都不可以
        if len(result) != 1:
            add_error_message(f'Cannot convert `{result}` into `CHAR`. ', self)
        else:
            return (result, 'CHAR')

class Real_convert(AST_Node):
    def __init__(self, expression, *args, **kwargs):
        self.type = 'REAL_CONVERT'
        self.expression = expression
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        result = self.expression.exe()
        if len(result) != 1:
            add_error_message(f'`{self.type}` could only convert one parameter. ', self)
            return
        else:
            result = result[0]
        try:
            result = float(result[0])
            return (result, 'REAL')
        except:
            add_error_message(f'Cannot convert `{result[0]}` into `REAL`. ', self)

class Bool_convert(AST_Node):
    def __init__(self, expression, *args, **kwargs):
        self.type = 'BOOLEAN_CONVERT'
        self.expression = expression
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        result = self.expression.exe()
        if len(result) != 1:
            add_error_message(f'`{self.type}` could only convert one parameter. ', self)
            return
        else:
            result = result[0]
        try:
            result = bool(result[0])
            return (result, 'BOOLEAN')
        except:
            add_error_message(f'Cannot convert `{result[0]}` into `BOOLEAN`. ', self)


class Right(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        self.type = 'RIGHT'
        self.parameters = parameters
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 2:
            add_error_message(f'Function `{self.type}` expect 2 parameters, but found `{len(parameters)}`. ', self)
            return

        s = parameters[0]
        x = parameters[1]
        if s[1] == 'STRING' and x[1] == 'INTEGER':
            return (s[0][len(s[0])-x[0]:], 'STRING')
        else:
            add_error_message(f'Function `{self.type}` expect `STRING` and `INTEGER`, but found `{s[1]}` and `{x[1]}`. ', self)

class Length(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        self.type = 'LENGTH'
        self.parameters = parameters
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 1:
            add_error_message(f'Function `{self.type}` expect 1 parameters, but found `{len(parameters)}`. ', self)
            return

        s = parameters[0]
        if s[1] == 'STRING' or s[1] == 'ARRAY':
            return (len(s[0]), 'INTEGER')
        else:
            add_error_message(f'Function `{self.type}` expect `STRING` or `ARRAY`, but found `{s[1]}`. ', self)

class Mid(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        self.type = 'MID'
        self.parameters = parameters
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 3:
            add_error_message(f'Function `{self.type}` expect 3 parameters, but found `{len(parameters)}`. ', self)
            return

        s = parameters[0]
        x = parameters[1]
        y = parameters[2]
        if s[1] == 'STRING' and x[1] == 'INTEGER' and y[1] == 'INTEGER':
            return (s[0][x[0]-1:x[0]+y[0]-1], 'STRING')
        else:
            add_error_message(f'Function `{self.type}` expect `STRING` and `INTEGER` and `INTEGER`, but found `{self.s[1]}` and `{self.x[1]}` and `{self.y[1]}`. ', self)

class Lcase(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        self.type = 'LCASE'
        self.parameters = parameters
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 1:
            add_error_message(f'Function `{self.type}` expect 1 parameters, but found `{len(parameters)}`. ', self)
            return

        c = parameters[0]
        if c[1] == 'CHAR':
            return (c[0].lower(), 'CHAR')
        else:
            add_error_message(f'Function `{self.type}` expect `CHAR`, but found `{c[1]}`. ', self)

class Ucase(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        self.type = 'UCASE'
        self.parameters = parameters
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 1:
            add_error_message(f'Function `{self.type}` expect 1 parameters, but found `{len(parameters)}`. ', self)
            return

        c = parameters[0]
        if c[1] == 'CHAR':
            return (c[0].upper(), 'CHAR')
        else:
            add_error_message(f'Function `{self.type}` expect `CHAR`, but found `{c[1]}`. ', self)


class Rand(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        self.type = 'RAND'
        self.parameters = parameters
        self.rate = 100
        super().__init__(*args, **kwargs)

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 1:
            add_error_message(f'Function `{self.type}` expect 1 parameters, but found `{len(parameters)}`. ', self)
            return

        n = parameters[0]
        if n[1] == 'INTEGER':
            return ( randint(0, n[0]*self.rate)/self.rate , "REAL")
        else:
            add_error_message(f'Function `{self.type}` expect `CHAR`, but found `{n[1]}`. ', self)


insert_functions = {
    "INT": Int_convert,
    "REAL": Real_convert,
    "STRING": Str_convert,
    "BOOLEAN": Bool_convert,
    "CHAR": Char_convert,
    "RIGHT": Right,
    "LENGTH": Length,
    "MID": Mid,
    "LCASE": Lcase,
    "UCASE": Ucase,
    "RAND": Rand,
}
