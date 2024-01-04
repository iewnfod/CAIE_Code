from .global_var import output_error, console
from .AST import stack
from sys import exit

def quit(code=0):
    stack.close_all_files()
    output_error()
    console.postloop()
    stack.delete()
    exit(code)
