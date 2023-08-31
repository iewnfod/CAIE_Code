from os import _exit
from .global_var import output_error, console

def quit(code=0):
    output_error()
    console.postloop()
    _exit(code)
