from src.lex import *
from src.parse import *
from ply import yacc
from ply import lex
import sys
import platform
import signal

VERSION = 'v0.1.0'
PLATFORM = f'[ {platform.python_implementation()} {platform.python_version()} ] on {platform.system()}'

show_tree = False

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


def with_input():
    # 基准输出
    standard_output()
    # 运行
    while 1:
        text = remove_comment(input('$ '))
        try:
            ast = parser.parse(text)
            ast.exe()
        except Exception as e:
            print('Error:', e)

def with_file(path):
    with open(path, 'r') as f:
        text = remove_comment(f.read())
    ast = parser.parse(text)
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

def version():
    print('Version:', VERSION)
    exit(0)

arguments = [  # 输入参数: (参数简写, 参数全称, 运行函数, 描述)
    ('-gt', '--get-tree', get_tree, 'To show the tree of the program after being parsed'),
    ('-v', '--version', version, 'To show the version of this interpreter'),
    ('-h', '--help', help, 'To show this help page')
]

def main():
    if len(sys.argv) == 1:
        with_input()
    else:
        for arg in sys.argv:
            for i in arguments:
                if arg == i[0] or arg == i[1]:
                    i[2]()
                    break
            else:
                path = arg

        with_file(path)

def ctrl_c_handle(signal, frame):
    print('\nKeyboard Interrupt\n$ ', end='')

if __name__ == '__main__':
    signal.signal(signal.SIGINT, ctrl_c_handle)

    lexer = lex.lex()
    parser = yacc.yacc()

    try:
        main()
    except EOFError:
        print("\nEXIT")
