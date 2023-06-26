from src.lex import *
from src.parse import *
from ply import yacc
from ply import lex

def remove_comment(text):
    text = text.split('\n')
    for i in range(len(text)):
        text[i] = text[i].split('//')[0]

    return '\n'.join(text)


def with_input():
    while 1:
        text = remove_comment(input('$ '))
        ast = parser.parse(text)
        ast.exe()

def with_file(path):
    with open(path, 'r') as f:
        text = remove_comment(f.read())
    parser.parse(text)


def main():
    with_input()

if __name__ == '__main__':
    lexer = lex.lex()
    parser = yacc.yacc()

    try:
        main()
    except KeyboardInterrupt:
        print(" Keyboard Interrupt ")
