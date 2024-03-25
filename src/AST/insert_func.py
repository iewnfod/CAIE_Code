from .data import *
from random import randint
from ..AST_Base import *
from ..global_var import *
from ..quit import *

def _wrong_param_number(name: str, expect_num: int, get_num: int, obj):
    add_error_message(f'Function `{name}` expect {expect_num} parameters, but found {get_num}', obj)

def _wrong_param_type(name: str, expect_types: list, get_types: list, obj):
    expect_type_list = [f'`{i}`' for i in expect_types]
    expect_type_str = ', '.join(expect_type_list)
    get_type_list = [f'`{i}`' for i in get_types]
    get_type_str = ', '.join(get_type_list)

    add_error_message(f'Function `{name}` expect parameter with type {expect_type_str}, but found {get_type_str}', obj)

class Int_convert(AST_Node):
    def __init__(self, expression, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'INTEGER_CONVERT'
        self.expression = expression

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        result = self.expression.exe()
        if len(result) != 1:
            _wrong_param_number("INT", 1, len(result), self)
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
        super().__init__(*args, **kwargs)
        self.type = 'STRING_CONVERT'
        self.expression = expression

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        result = self.expression.exe()
        if len(result) != 1:
            _wrong_param_number("STRING", 1, len(result), self)
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
        super().__init__(*args, **kwargs)
        self.type = 'CHAR_CONVERT'
        self.expression = expression

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        result = self.expression.exe()
        if len(result) != 1:
            _wrong_param_number("CHAR", 1, len(result), self)
            return
        else:
            result = result[0]


        try:
            result = str(result[0])
        except:
            add_error_message(f'Cannot convert `{result[0]}` into `CHAR`', self)
            return

        # 判断长度，如果不是1，都不可以
        if len(result) != 1:
            add_error_message(f'Cannot convert `{result}` into `CHAR`', self)
        else:
            return (result, 'CHAR')

class Real_convert(AST_Node):
    def __init__(self, expression, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'REAL_CONVERT'
        self.expression = expression

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        result = self.expression.exe()
        if len(result) != 1:
            _wrong_param_number("REAL", 1, len(result), self)
            return
        else:
            result = result[0]
        try:
            result = float(result[0])
            return (result, 'REAL')
        except:
            add_error_message(f'Cannot convert `{result[0]}` into `REAL`', self)

class Bool_convert(AST_Node):
    def __init__(self, expression, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'BOOLEAN_CONVERT'
        self.expression = expression

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def exe(self):
        result = self.expression.exe()
        if len(result) != 1:
            _wrong_param_number("BOOLEAN", 1, len(result), self)
            return
        else:
            result = result[0]
        try:
            result = bool(result[0])
            return (result, 'BOOLEAN')
        except:
            add_error_message(f'Cannot convert `{result[0]}` into `BOOLEAN`', self)


class Left(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'LEFT'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 2:
            _wrong_param_number("LEFT", 2, len(parameters), self)
            return

        s = parameters[0]
        x = parameters[1]
        if s[1] == 'STRING' and x[1] == 'INTEGER':
            return (s[0][0:x[0]], 'STRING')
        else:
            _wrong_param_type("LEFT", ['STRING', 'INTEGER'], [s[1], x[1]], self)

class Right(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'RIGHT'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 2:
            _wrong_param_number("RIGHT", 2, len(parameters), self)
            return

        s = parameters[0]
        x = parameters[1]
        if s[1] == 'STRING' and x[1] == 'INTEGER':
            return (s[0][len(s[0])-x[0]:], 'STRING')
        else:
            _wrong_param_type("RIGHT", ['STRING', 'INTEGER'], [s[1], x[1]], self)

class Length(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'LENGTH'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 1:
            _wrong_param_number("LENGTH", 1, len(parameters), self)
            return

        s = parameters[0]
        if s[1] == 'STRING':
            return (len(s[0]), 'INTEGER')
        elif s[1] == 'ARRAY':
            return (len(s), 'INTEGER')
        else:
            _wrong_param_type("LENGTH", ['STRING'], [s[1]], self)

class Mid(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'MID'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 3:
            _wrong_param_number("MID", 3, len(parameters), self)
            return

        s = parameters[0]
        x = parameters[1]
        y = parameters[2]
        if s[1] == 'STRING' and x[1] == 'INTEGER' and y[1] == 'INTEGER':
            return (s[0][x[0]-1:x[0]+y[0]-1], 'STRING')
        else:
            _wrong_param_type("MID", ['STRING', 'INTEGER', 'INTEGER'], [s[1], x[1], y[1], self])

class Lcase(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'LCASE'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(parameters) != 1:
                _wrong_param_number(self.type, 1, len(parameters), self)
                return

            c = parameters[0]
            if c[1] == 'CHAR':
                return (c[0].lower(), 'CHAR')
            elif c[1] == 'STRING':
                return (c[0].lower(), 'STRING')
            else:
                _wrong_param_type(self.type, ['CHAR', 'STRING'], [c[1]], self)
        else:
            _wrong_param_number(self.type, 1, 0, self)

class Ucase(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'UCASE'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(parameters) != 1:
                _wrong_param_number(self.type, 1, len(parameters), self)
                return

            c = parameters[0]
            if c[1] == 'CHAR':
                return (c[0].upper(), 'CHAR')
            elif c[1] == 'STRING':
                return (c[0].upper(), 'STRING')
            else:
                _wrong_param_type(self.type, ['CHAR', 'STRING'], [c[1]], self)
        else:
            _wrong_param_number(self.type, 1, 0, self)


class Rand(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'RAND'
        self.parameters = parameters
        self.rate = 100

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 1:
            _wrong_param_number("RAND", 1, len(parameters), self)
            return

        n = parameters[0]
        if n[1] == 'INTEGER':
            return ( randint(0, n[0]*self.rate)/self.rate , "REAL")
        else:
            _wrong_param_type("RAND", ['INTEGER'], [n[1]], self)


class Eof(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'EOF'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        parameters = self.parameters.exe()
        if len(parameters) != 1:
            _wrong_param_number("EOF", 1, len(parameters), self)
            return

        fp = parameters[0]
        if fp[1] == 'STRING':
            f = stack.get_file(fp[0])
            eof = stack.get_eof(fp[0])
            if f.tell() >= eof:
                return (True, 'BOOLEAN')
            else:
                return (False, 'BOOLEAN')
        else:
            _wrong_param_type("EOF", ['STRING'], [fp[1]], self)

class Pow(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'POW'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(self.parameters) == 2:
                p = parameters[0]
                if p[1] == 'INTEGER' or p[1] == 'REAL':
                    try:
                        return (parameters[0][0] ** parameters[1][0], 'REAL')
                    except:
                        add_error_message(f'Cannot power `{parameters[0][1]}` with `{parameters[1][1]}`', self)
                else:
                    _wrong_param_type("POW", ['REAL'], [p[1]], self)

class Exit(AST_Node):
    def __init__(self, parameters=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'EXIT'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        if self.parameters != None:
            parameters = self.parameters.exe()
            try:
                exit_code = int(parameters[0][0])
            except:
                exit_code = 0
        else:
            exit_code = 0

        quit(exit_code)

class Round(AST_Node):
    def __init__(self, parameters=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'ROUND'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(self.parameters) == 1:
                if parameters[0][1] == 'INTEGER':
                    return (round(parameters[0][0]), 'INTEGER')
            elif len(self.parameters) == 2:
                if parameters[0][1] == 'REAL' and parameters[1][1] == 'INTEGER':
                    return (round(parameters[0][0], parameters[1][0]), 'REAL')
            else:
                add_error_message(f'Function `ROUND` expect 1 or 2 parameters, but found {len(self.parameters)}', self)
        else:
            add_error_message(f'Function `ROUND` expect 1 or 2 parameters, but found 0', self)

class Python(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'PYTHON'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            code = parameters[0][0]
            global_space = {}

            # 尝试导入参数
            for i in range(1, len(parameters)):
                try:
                    global_space[self.parameters.parameters[i].id] = parameters[i][0]
                except:
                    add_error_message(f'`PYTHON` interface only accept variables with basic data types', self)

            return_name = '_result'
            global_space[return_name] = None

            try:
                exec(code, global_space)
            except Exception as e:
                add_python_error_message(e, self)
                # global_space[return_name] = None

            return (global_space[return_name], None)  # None 表示未知类型
        else:
            add_error_message(f'`PYTHON` interface only have 1 parameters, but found 0', self)

class Mod(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'MOD'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(self.parameters) == 2:
                return (parameters[0][0] % parameters[1][0], 'REAL')
            else:
                _wrong_param_number("MOD", 2, len(self.parameters), self)
        else:
            _wrong_param_number("MOD", 2, 0, self)

class Div(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'DIV'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(self.parameters) == 2:
                return (parameters[0][0] // parameters[1][0], 'REAL')
            else:
                _wrong_param_number("DIV", 2, len(self.parameters), self)
        else:
            _wrong_param_number("DIV", 2, len(self.parameters), self)

class VarType(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'VAR_TYPE'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)

    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(parameters) == 1:
                return (parameters[0][1], 'STRING')
            else:
                _wrong_param_number("VARTYPE", 1, len(parameters), self)
        else:
            _wrong_param_number("VARTYPE", 1, 0, self)

class ToUpper(Ucase):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(parameters, *args, **kwargs)
        self.type = 'TO_UPPER'

class ToLower(Lcase):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(parameters, *args, **kwargs)
        self.type = 'TO_LOWER'

class Day(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'DAY'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)
    
    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(parameters) == 1:
                p = parameters[0]
                if p[1] == 'DATE':
                    return (int(p[0].split('/')[0]), 'INTEGER')
                else:
                    _wrong_param_type("DAY", ['DATE'], [p[1]], self)
            else:
                _wrong_param_number("DAY", 1, len(parameters), self)
        else:
            _wrong_param_number("DAY", 1, 0, self)

class Month(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'MONTH'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)
    
    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(parameters) == 1:
                p = parameters[0]
                if p[1] == 'DATE':
                    return (int(p[0].split('/')[1]), 'INTEGER')
                else:
                    _wrong_param_type("MONTH", ['DATE'], [p[1]], self)
            else:
                _wrong_param_number("MONTH", 1, len(parameters), self)
        else:
            _wrong_param_number("MONTH", 1, 0, self)

class Year(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'YEAR'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)
    
    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(parameters) == 1:
                p = parameters[0]
                if p[1] == 'DATE':
                    return (int(p[0].split('/')[2]), 'INTEGER')
                else:
                    _wrong_param_type("YEAR", ['DATE'], [p[1]], self)
            else:
                _wrong_param_number("YEAR", 1, len(parameters), self)
        else:
            _wrong_param_number("YEAR", 1, 0, self)

class DayIndex(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'DAY_INDEX'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)
    
    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(parameters) == 1:
                p = parameters[0]
                if p[1] == 'DATE':
                    from datetime import datetime
                    return (datetime.strptime(p[0], '%d/%m/%Y').weekday() + 1) % 7 + 1
                else:
                    _wrong_param_type("DAYINDEX", ['DATE'], [p[1]], self)
            else:
                _wrong_param_number("DAYINDEX", 1, len(parameters), self)
        else:
            _wrong_param_number("DAYINDEX", 1, 0, self)

class SetDate(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'SET_DATE'
        self.parameters = parameters

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.parameters.get_tree(level+1)
    
    def exe(self):
        if self.parameters:
            parameters = self.parameters.exe()
            if len(self.parameters) == 3:
                p = parameters[0]
                if p[1] == 'INTEGER':
                    return (f'{parameters[0][0]:02}/{parameters[1][0]:02}/{parameters[2][0]:04}', 'DATE')
                else:
                    _wrong_param_type("SETDATE", ['INTEGER', 'INTEGER', 'INTEGER'], [p[1]], self)
            else:
                _wrong_param_number("SETDATE", 3, len(parameters), self)
        else:
            _wrong_param_number("SETDATE", 3, 0, self)

class Today(AST_Node):
    def __init__(self, parameters, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'TODAY'

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type

    def exe(self):
        if not self.parameters:
            from datetime import datetime
            return (datetime.now().strftime('%d/%m/%Y'), 'DATE')
        else:
            parameters = self.parameters.exe()
            _wrong_param_number("TODAY", 0, len(parameters), self)

insert_functions = {
    "INT": Int_convert,
    "INTEGER": Int_convert,
    "REAL": Real_convert,
    "STRING": Str_convert,
    "BOOLEAN": Bool_convert,
    "CHAR": Char_convert,
    "LEFT": Left,
    "RIGHT": Right,
    "LENGTH": Length,
    "MID": Mid,
    "LCASE": Lcase,
    "UCASE": Ucase,
    "RAND": Rand,
    "RANDOM": Rand,
    "EOF": Eof,
    "POW": Pow,
    "EXIT": Exit,
    "ROUND": Round,
    "PYTHON": Python,
    "MOD": Mod,
    "DIV": Div,
    "VARTYPE": VarType,
    "TO_UPPER": ToUpper,
    "TO_LOWER": ToLower,
    "DAY": Day,
    "MONTH": Month,
    "YEAR": Year,
    "DAYINDEX": DayIndex,
    "SETDATE": SetDate,
    "TODAY": Today
}
