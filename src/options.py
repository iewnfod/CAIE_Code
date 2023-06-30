import platform
import sys

VERSION = 'v0.1.0'
PLATFORM = f'[ {platform.python_implementation()} {platform.python_version()} ] on {platform.system()}'

def standard_output():
    print(f'CAIE Pseudocode Interpreter {VERSION}')
    print(f'Base on {PLATFORM}')
    print('Submit issues at https://github.com/iewnfod/CAIE_Code/issues/new')
    print('Copyright (c) 2023 Iewnfod. ')
    print('All Rights Reserved. ')

def open_debug():
    global debug
    debug = True

def version():
    print('Version:', VERSION)
    sys.exit(0)

def help():
    standard_output()

    print()

    print('Usage: [file_path] [options]')

    print()

    print('Options:')
    arguments.sort()
    for i in arguments:
        print('\t', i[0], '\t', i[1], '\t', i[3])

    sys.exit(0)

def get_tree():
    global show_tree
    show_tree = True


arguments = [  # 输入参数: (参数简写, 参数全称, 运行函数, 描述)
    ('-gt', '--get-tree', get_tree, 'To show the tree of the program after being parsed'),
    ('-v', '--version', version, 'To show the version of this interpreter'),
    ('-h', '--help', help, 'To show this help page'),
    ('-d', '--debug', open_debug, 'To show debug information during running'),
]
