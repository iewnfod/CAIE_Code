class Error:
    def __init__(self, message, ast_obj):
        self.message = message
        self.ast_obj = ast_obj

    def raise_err(self):
        print(f'\033[1;31mError\033[0m: \033[1m{self.message}\033[0m {self.ast_obj.get_pos()}')

class StackError:
    def __init__(self, message):
        self.message = str(message)

    def raise_err(self):
        print(f'\033[1;31mStack Error\033[0m: \033[1m{self.message}\033[0m')
