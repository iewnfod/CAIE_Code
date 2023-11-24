from os import _exit
from .global_var import output_error, console
from .AST import stack

def quit(code=0):
    stack.close_all_files()
    output_error()
    console.postloop()
    stack.delete()
    _exit(code)
