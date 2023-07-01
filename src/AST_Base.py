class AST_Node:
    def __init__(self, lineno=0, lexpos=0):
        self.lineno = lineno
        self.lexpos = lexpos

    def get_pos(self):
        return f'line {self.lineno}'
