from .error import *
from . import options
from .history import Cmd

error_messages = []
running_mod = 'file'  # file / line
running_path = ''  # 当前运行文件
console = Cmd()

# 变量
def __init__():
    global error_messages, running_mod
    error_messages = []
    running_mod = 'file'
    console.preloop()

def add_error_message(msg, obj):
    error_messages.append(Error(msg, obj))

def get_error_messages():
    return error_messages

def clear_error_messages():
    global error_messages
    error_messages = []

def add_stack_error_message(msg):
    error_messages.append(StackError(msg))

def add_python_error_message(msg, obj):
    error_messages.append(PythonError(msg, obj))

def add_parse_error_message(msg, obj):
    error_messages.append(ParseError(msg, obj))

def add_eof_error_message(obj):
    error_messages.append(EofError(obj))

def add_lexer_error_message(msg, obj):
    error_messages.append(LexerError(msg, obj))

def set_running_mod(mod):
    global running_mod
    running_mod = mod

def get_running_mod():
    return running_mod

def set_running_path(p):
    global running_path
    running_path = p

# 输出错误信息
def output_error():
    if not options.get_value('show_error'):
        # 如果不显示错误信息
        # 清空错误并直接返回
        clear_error_messages()
        return

    errors = get_error_messages()
    errors.sort()
    l = set()
    for i in errors:
        if i not in l:
            l.add(i)

    if l:
        # 输出文件路径
        if running_path:
            print(f'File `{running_path}`: ')
        # 输出错误信息
        for i in l:
            print('\t' if running_path else '', end='')
            i.raise_err()
        # 清空错误数组
        clear_error_messages()
