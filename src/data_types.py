from copy import deepcopy

class base:
    def __init__(self, name=None):
        self.name = name
        self.is_struct = False

    def __str__(self):
        return str(self.value)

    def __getitem__(self, key):
        if key == 1:
            return self.type
        else:
            return self.value

class INTEGER(base):
    def __init__(self, value=0, *args, **kwargs):
        self.value = int(value)
        self.type = 'INTEGER'
        super().__init__(*args, **kwargs)

    def set_value(self, new_value):
        self.value = int(new_value)

    def __bool__(self):
        return bool(self.value)

class REAL(base):
    def __init__(self, value=.0, *args, **kwargs):
        self.value = float(value)
        self.type = 'REAL'
        super().__init__(*args, **kwargs)

    def set_value(self, new_value):
        self.value = float(new_value)

class STRING(base):
    def __init__(self, value='', *args, **kwargs):
        self.value = str(value)
        self.type = 'STRING'
        super().__init__(*args, **kwargs)

    def set_value(self, new_value):
        self.value = str(new_value)

    def __str__(self):
        return '"' + self.value + '"'

class CHAR(base):
    def __init__(self, value='', *args, **kwargs):
        self.set_value(value)
        self.type = 'CHAR'
        super().__init__(*args, **kwargs)

    def set_value(self, new_value):
        if new_value == '':
            self.value = ''
        else:
            self.value = str(new_value)[0]

    def __str__(self):
        return "'" + self.value + "'"

class BOOLEAN(base):
    def __init__(self, value=False, *args, **kwargs):
        if value == 'FALSE':
            self.value = False
        elif value == 'TRUE':
            self.value = True
        else:
            self.value = bool(value)
        self.type = 'BOOLEAN'
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        return {True: 'TRUE', False: 'FALSE'}[self.value]

    def set_value(self, new_value):
        self.value = bool(new_value)

import time
class DATE(base):
    def __init__(self, value=time.strftime("%d/%m/%Y", time.localtime()), *args, **kwargs):
        self.day, self.month, self.year = value.split('/')
        self.type = 'DATE'
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'

    def __getitem__(self, key):
        if key == 1:
            return self.type
        else:
            return (self.year, self.month, self.day)

    def set_value(self, new_value):
        self.year, self.month, self.day = new_value

class ARRAY(base):
    def __init__(self, value={}, *args, **kwargs):
        self.value = value
        self.type = 'ARRAY'
        super().__init__(*args, **kwargs)

    def get_str(self, v):
        if v[1] == 'ARRAY':
            l = []
            for key, val in v[0][0].items():
                if key == 'left' or key == 'right': continue
                l.append(self.get_str(val))
            return '[' + ', '.join(l) + ']'
        else:
            return str(v[0])

    def __str__(self) -> str:
        l = []
        for key, val in self.value.items():
            if key == 'left' or key == 'right': continue
            l.append(self.get_str(val))
        return '[' + ', '.join(l) + ']'

    def __len__(self):
        return len(self.value) - 2  # 减掉left和right

    def set_value(self, value):
        from .global_var import add_stack_error_message
        if value['left'] == self.value['left'] and value['right'] == self.value['right']:
            self.value = value
            # self.to_target(list(value.items())[0][1][1])
        else:
            s_left = self.value['left']
            s_right = self.value['right']
            left = self.value['left']
            right = self.value['right']
            add_stack_error_message(f'Cannot assign an array with size `{left}:{right}` to an array with size `{s_left}:{s_right}`')

    def to_target(self, target, v=None):
        from .AST.data import stack
        from .global_var import add_stack_error_message
        if v == None:
            v = self.value
        for i in v.keys():
            if v[i][1] == 'ARRAY':
                self.to_target(target, v[i])
            else:
                # 如果不是目标类型，则需要转换
                if v[i][1] != target:
                    try:
                        v[i] = stack.structs[target](v[i][0])
                    except:
                        add_stack_error_message(f'Cannot change value `{str(v[i][0])}` into `{target}`')

from enum import Enum
class ENUM(base):
    def __init__(self, *args, **kwargs):
        self.value = None
        self.type = 'ENUM'
        super().__init__(*args, **kwargs)

    def set_value(self, value):
        self.value = Enum(self.name, value)
