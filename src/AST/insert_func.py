from src.AST.data import *

class Int_convert:
    def __init__(self, expression):
        self.type = 'INTEGER_CONVERT'
        self.expression = expression

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        result = self.expression.exe()
        if len(result) != 1:
            print(f'`{self.type}` could only convert one parameter.')
            return
        else:
            result = result[0]
        try:
            result = int(result[0])
            return (result, 'INTEGER')
        except:
            print(f'Cannot convert `{result[0]}` into `INTEGER`')

class Str_convert:
    def __init__(self, expression):
        self.type = 'STRING_CONVERT'
        self.expression = expression

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        result = self.expression.exe()
        if len(result) != 1:
            print(f'`{self.type}` could only convert one parameter.')
            return
        else:
            result = result[0]
        try:
            result = str(result[0])
            return (result, 'STRING')
        except:
            print(f'Cannot convert `{result[0]}` into `STRING`')

class Char_convert:
    def __init__(self, expression):
        self.type = 'CHAR_CONVERT'
        self.expression = expression

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        result = self.expression.exe()
        if len(result) != 1:
            print(f'`{self.type}` could only convert one parameter.')
            return
        else:
            result = result[0]


        try:
            result = str(result[0])
        except:
            print(f'Cannot convert `{result[0]}` into `CHAR`')
            return

        # 判断长度，如果不是1，都不可以
        if len(result) != 1:
            print(f'Cannot convert `{result}` into `CHAR`')
        else:
            return (result, 'CHAR')

class Real_convert:
    def __init__(self, expression):
        self.type = 'REAL_CONVERT'
        self.expression = expression

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        result = self.expression.exe()
        if len(result) != 1:
            print(f'`{self.type}` could only convert one parameter.')
            return
        else:
            result = result[0]
        try:
            result = float(result[0])
            return (result, 'REAL')
        except:
            print(f'Cannot convert `{result[0]}` into `REAL`')

class Bool_convert:
    def __init__(self, expression):
        self.type = 'BOOLEAN_CONVERT'
        self.expression = expression

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        result = self.expression.exe()
        if len(result) != 1:
            print(f'`{self.type}` could only convert one parameter.')
            return
        else:
            result = result[0]
        try:
            result = bool(result[0])
            return (result, 'BOOLEAN')
        except:
            print(f'Cannot convert `{result[0]}` into `BOOLEAN`')


class Right:
    def __init__(self, parameters):
        self.type = 'RIGHT'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.s.get_tree(level+1) + '\n' + self.x.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 2:
            print(f'Function `{self.type}` expect 2 parameters, but found `{len(parameters)}`')
            return

        s = parameters[0]
        x = parameters[1]
        if s[1] == 'STRING' and x[1] == 'INTEGER':
            return (s[0][len(s[0])-x[0]:], 'STRING')
        else:
            print(f'Function `{self.type}` expect `STRING` and `INTEGER`, but found `{s[1]}` and `{x[1]}`')

class Length:
    def __init__(self, parameters):
        self.type = 'LENGTH'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.s.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 1:
            print(f'Function `{self.type}` expect 1 parameters, but found `{len(parameters)}`')
            return

        s = parameters[0]
        if s[1] == 'STRING':
            return (len(s[0]), 'INTEGER')
        else:
            print(f'Function `{self.type}` expect `STRING`, but found `{s[1]}')

class Mid:
    def __init__(self, parameters):
        self.type = 'MID'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.s.get_tree(level+1) + '\n' + self.x.get_tree(level+1) + '\n' + self.y.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 3:
            print(f'Function `{self.type}` expect 3 parameters, but found `{len(parameters)}`')
            return

        s = parameters[0]
        x = parameters[1]
        y = parameters[2]
        if s[1] == 'STRING' and x[1] == 'INTEGER' and y[1] == 'INTEGER':
            return (s[0][x[0]-1:x[0]+y[0]-1], 'STRING')
        else:
            print(f'Function `{self.type}` expect `STRING` and `INTEGER` and `INTEGER`, but found `{self.s[1]}` and `{self.x[1]}` and `{self.y[1]}`')

class Lcase:
    def __init__(self, parameters):
        self.type = 'LCASE'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.c.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 1:
            print(f'Function `{self.type}` expect 1 parameters, but found `{len(parameters)}`')
            return

        c = parameters[0]
        if c[1] == 'CHAR':
            return (c[0].lower(), 'CHAR')
        else:
            print(f'Function `{self.type}` expect `CHAR`, but found `{c[1]}`')

class Ucase:
    def __init__(self, parameters):
        self.type = 'UCASE'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.c.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 1:
            print(f'Function `{self.type}` expect 1 parameters, but found `{len(parameters)}`')
            return

        c = parameters[0]
        if c[1] == 'CHAR':
            return (c[0].upper(), 'CHAR')
        else:
            print(f'Function `{self.type}` expect `CHAR`, but found `{c[1]}`')


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
}
