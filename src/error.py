class Error:
    def __init__(self, message, ast_obj):
        self.message = message
        self.ast_obj = ast_obj

    def raise_err(self):
        print(f'Error: {self.message} {self.ast_obj.get_pos()}')

class StackError:
    def __init__(self, message):
        self.message = str(message)

    def raise_err(self):
        print(f'Stack Error: {self.message}')
