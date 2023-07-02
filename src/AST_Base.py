class AST_Node:
    def __init__(self, lineno=0, lexpos=0):
        self.lineno = lineno
        self.lexpos = lexpos

    def get_pos(self):
        if self.lineno:
            return f'at line {self.lineno}'
        else:
            return ''
