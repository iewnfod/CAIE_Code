from .AST_Base import AST_Node

class Error:
    def __init__(self, message, ast_obj):
        self.message = message
        self.ast_obj = ast_obj

    def raise_err(self):
        print(f'\033[1;31mError\033[0m: \033[1m{self.message}\033[0m {self.ast_obj.get_pos()}')

    def __lt__(self, other):
        return self.ast_obj.get_pos() < other.ast_obj.get_pos()

class StackError(Error):
    def __init__(self, message):
        super().__init__(message, AST_Node())

    def raise_err(self):
        print(f'\033[1;31mStack Error\033[0m: \033[1m{self.message}\033[0m')

class PythonError(Error):
    def __init__(self, e, ast_obj):
        super().__init__(e, ast_obj)

    def raise_err(self):
        print(f'\033[1;31mPython Error\033[0m: \033[1m{self.message}\033[0m {self.ast_obj.get_pos()}')
