from os import _exit
from .global_var import output_error

def quit(code):
    output_error()
    _exit(code)
