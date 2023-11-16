from .data import *
from ..AST_Base import *
from ..global_var import *
from .array import *
from .data_types import *

class Output(AST_Node):
    def __init__(self, value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'OUTPUT'
        self.value = value

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.value.get_tree(level+1)

    def exe(self):
        v = self.value.exe()
        print_(v if v != None else '')

class Output_expression(AST_Node):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'OUTPUT_EXPRESSION'
        self.expressions = []

    def get_tree(self, level=0):
        r = LEVEL_STR * level + self.type
        for i in self.expressions:
            r += '\n' + i.get_tree(level+1)
        return r

    def add_expression(self, expression):
        self.expressions.append(expression)

    def exe(self):
        result = ''
        for i in self.expressions:
            t = i.exe()
            if t[1] == 'ARRAY':
                result += str(t)
            elif t[1] == 'BOOLEAN':
                result += {True: 'TRUE', False: 'FALSE'}[t[0]]
            else:
                result += str(t[0])
        return result

class Input(AST_Node):
    def __init__(self, id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'INPUT'
        self.id = id

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id)

    def exe(self):
        stack.set_variable(self.id, str(input_()), 'STRING')

class Array_input(AST_Node):
    def __init__(self, id, indexes, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'ARRAY_INPUT'
        self.id = id
        self.indexes = indexes

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + ' ' + str(self.id) + '\n' + self.indexes.get_tree(level+1)

    def exe(self):
        inp = input()
        Array_assign(
            self.id,
            self.indexes,
            String(inp, lineno=self.lineno, lexpos=self.lexpos),
            lineno=self.lineno,
            lexpos=self.lexpos
        ).exe()

class Raw_output(AST_Node):
    def __init__(self, expression, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 'RAW_OUTPUT'
        self.expression = expression

    def get_tree(self, level=0):
        return LEVEL_STR * level + self.type + '\n' + self.expression.get_tree(level+1)

    def _output(self, v):
        # 如果当前是文件模式，那么就应该输出此方法的结果
        if get_running_mod() == 'file': need_output = False
        else: need_output = True

        if need_output: print_(v)

    def exe(self):
        t = self.expression.exe()
        v = t[0] if type(t) == tuple else str(t)
        # 如果是 tuple，那就看类型，并输出
        if type(t) == tuple:
            if t[1] == 'STRING':
                self._output('"' + v + '"')
            elif t[1] == 'CHAR':
                self._output("'" + v + "'")
            elif t[1] == 'BOOLEAN':
                self._output({True: 'TRUE', False: 'FALSE'}[v])
            else:
                self._output(v)
        else:
            self._output(v)
