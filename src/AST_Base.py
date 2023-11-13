class AST_Node:
    def __init__(self, p=None):
        self.p = p
        if self.p:
            try:
                self.lineno = self.p.lineno(0)
                self.lexpos = self.p.lexpos(0)
            except:
                self.lineno = self.p.lineno
                self.lexpos = self.p.lexpos
        else:
            self.lineno = 0
            self.lexpos = 0

    def get_pos(self):
        if self.lineno:
            return f'at line {self.lineno}'
        else:
            return ''
