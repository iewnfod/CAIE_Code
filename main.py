from src.lex import *
from src.parse import *
from ply import yacc
from ply import lex
import sys
import platform

VERSION = 'v0.1.0'
PLATFORM = f'[ {platform.python_implementation()} {platform.python_version()} ] on {platform.version()}'

def remove_comment(text):
    text = text.split('\n')
    for i in range(len(text)):
        text[i] = text[i].split('//')[0]

    return '\n'.join(text)


def with_input():
    # 基准输出
    print(f'CAIE Pseudocode Interpreter {VERSION}')
    print(PLATFORM)
    print('Submit issues at https://github.com/iewnfod/CAIE_Code/issues/new')
    print('Copyright (c) 2023 Iewnfod')
    print('All Rights Reserved')
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
    ast.exe()


def main():
    if len(sys.argv) == 1:
        with_input()
    else:
        with_file(sys.argv[1])

if __name__ == '__main__':
    lexer = lex.lex()
    parser = yacc.yacc()

    try:
        main()
    except KeyboardInterrupt:
        print(" Keyboard Interrupt ")
