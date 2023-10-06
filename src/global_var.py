from .error import *
from . import options
from .history import Cmd
import sys

errors = {}
running_mod = 'file'  # file / line
running_path = ''  # 当前运行文件
console = Cmd()
std_in = sys.stdin
std_out = sys.stdout

# 变量
def __init__():
    global errors, running_mod
    errors = {}
    running_mod = 'file'
    console.preloop()

def set_std_in(new_in):
    global std_in
    std_in = new_in

def set_std_out(new_out):
    global std_out
    std_out = new_out

def get_std_in():
    return std_in

def get_std_out():
    return std_out

def add_error_message(msg, obj):
    errors[running_path].append(Error(msg, obj))

def is_error_messages_empty():
    for i in errors.values():
        # 一旦有一个不是空的，那就有错误，就返回 False
        if i: return False
    # 全都没错，才是真的没错
    return True

def clear_error_messages():
    global errors
    keys = errors.keys()
    errors = {}
    for key in keys:
        errors[key] = []

def add_stack_error_message(msg):
    errors[running_path].append(StackError(msg))

def add_python_error_message(msg, obj):
    errors[running_path].append(PythonError(msg, obj))

def add_parse_error_message(msg, obj):
    errors[running_path].append(ParseError(msg, obj))

def add_eof_error_message(obj):
    errors[running_path].append(EofError(obj))

def add_lexer_error_message(msg, obj):
    errors[running_path].append(LexerError(msg, obj))

def set_running_mod(mod):
    global running_mod
    running_mod = mod

def get_running_mod():
    return running_mod

def set_running_path(p):
    global running_path
    running_path = p
    errors[running_path] = []

def get_running_path():
    return running_path

def print_(t, end='\n'):
    get_std_out().write(str(t) + end)
    get_std_out().flush()

def input_():
    get_std_out().flush()
    return get_std_in().readline()

# 输出错误信息
def output_error():
    if not options.get_value('show_error'):
        # 如果不显示错误信息
        # 清空错误并直接返回
        clear_error_messages()
        return

    for path, errs in errors.items():
        errs.sort()
        l = set()
        for i in errs:
            if i not in l:
                l.add(i)

        if l:
            # 输出文件路径
            if path:
                print_(f'File `{path}`: ')
            # 输出错误信息
            for i in l:
                print_('\t' if path else '', end='')
                i.raise_err()

    # 清空错误
    clear_error_messages()
