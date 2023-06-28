from src.lex import *
from src.parse import *
from src.status import *
from ply import yacc
from ply import lex
import sys
import platform
import signal
import os

VERSION = 'v0.1.0'
PLATFORM = f'[ {platform.python_implementation()} {platform.python_version()} ] on {platform.system()}'

preline = '$'

def remove_comment(text):
    text = text.split('\n')
    for i in range(len(text)):
        text[i] = text[i].split('//')[0]

    return '\n'.join(text)


def standard_output():
    print(f'CAIE Pseudocode Interpreter {VERSION}')
    print(f'Base on {PLATFORM}')
    print('Submit issues at https://github.com/iewnfod/CAIE_Code/issues/new')
    print('Copyright (c) 2023 Iewnfod. ')
    print('All Rights Reserved. ')


def with_line():
    # 基准输出
    standard_output()
    # 运行
    while 1:
        text = remove_comment(input(f'{preline} '))
        try:
            ast = parser.parse(text, debug=debug)
            if show_tree:
                print(ast.get_tree())
            ast.exe()
        except Exception as e:
            print('Error:', e)

def with_file(path):
    with open(path, 'r') as f:
        text = remove_comment(f.read())
    ast = parser.parse(text, debug=debug)
    if show_tree:
        print(ast.get_tree())
    ast.exe()

def help():
    standard_output()

    print()

    print('Usage: [file_path] [options]')

    print()

    print('Options:')
    arguments.sort()
    for i in arguments:
        print('\t', i[0], '\t', i[1], '\t', i[3])

    exit(0)

def get_tree():
    global show_tree
    show_tree = True

def open_debug():
    global debug
    debug = True

def version():
    print('Version:', VERSION)
    exit(0)

arguments = [  # 输入参数: (参数简写, 参数全称, 运行函数, 描述)
    ('-gt', '--get-tree', get_tree, 'To show the tree of the program after being parsed'),
    ('-v', '--version', version, 'To show the version of this interpreter'),
    ('-h', '--help', help, 'To show this help page'),
    ('-d', '--debug', open_debug, 'To show debug information during running'),
]

def wrong_argument(msg):
    print(f'Wrong arguments: \033[1m{msg}\033[0m\n')
    help()

def main():
    # 解析参数
    file_path = ''
    for arg in sys.argv[1:]:
        for i in arguments:
            if arg == i[0] or arg == i[1]:
                i[2]()
                break
        else:
            file_path = arg

    # 选择模式运行
    if not file_path:
        with_line()
    else:
        if os.path.exists(file_path):
            if os.path.isfile(file_path):
                with_file(file_path)
            else:
                wrong_argument(f'`{file_path}` is not a file')
        else:
            wrong_argument(f'`{file_path}` does not exist')

def ctrl_c_handle(signal, frame):
    print(f'\nKeyboard Interrupt\n{preline} ', end='')

if __name__ == '__main__':
    signal.signal(signal.SIGINT, ctrl_c_handle)

    lexer = lex.lex()
    parser = yacc.yacc()

    try:
        main()
    except EOFError:
        print("\nEXIT")
        exit(0)
