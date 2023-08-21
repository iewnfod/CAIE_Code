from .error import Error, StackError

error_messages = []
running_mod = 'file'  # file / line

# 变量
def __init__():
    global error_messages, running_mod
    error_messages = []
    running_mod = 'file'

def add_error_message(msg, obj):
    error_messages.append(Error(msg, obj))

def get_error_messages():
    return error_messages

def clear_error_messages():
    global error_messages
    error_messages = []

def add_stack_error_messages(msg):
    error_messages.append(StackError(msg))

def set_running_mod(mod):
    global running_mod
    running_mod = mod

def get_running_mod():
    return running_mod
