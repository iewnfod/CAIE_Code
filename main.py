from src.lex import *
from src.parse import *
from src.status import *
from src.options import *
from ply import yacc
from ply import lex
import sys
import signal
import os
import chardet

preline = '$'

# 清除注释以及多余字符
def remove_comment(text):
    text = text.split('\n')
    for i in range(len(text)):
        text[i] = text[i].split('//')[0]

    return '\n'.join(text).strip()

# 预加载文件
def preload_scripts():
    for p, dir_list, file_list in os.walk('scripts'):
        for i in file_list:
            path = os.path.join(p, i)
            _, n = os.path.splitext(path)
            if n == '.cpc':
                with_file(path, True)

# 终端模式，逐行输入并解析运行
def with_line():
    # 基准输出
    standard_output()
    # 运行
    while 1:
        text = remove_comment(input(f'{preline} '))
        if not text:
            continue
        try:
            ast = parser.parse(text, debug=debug)
            if show_tree:
                print(ast.get_tree())
            ast.exe()
        except Exception as e:
            print('Error:', e)

# 文件模式，读取文件并解析运行
def with_file(path, preload=False):
    # 恢复行数，也就是不计算预加载文件的行数
    lexer.lineno = 1
    # 读取文件编码
    with open(path, 'rb') as f:
        encode = chardet.detect(f.read())['encoding']
    # 读取文件
    with open(path, 'r', encoding=encode) as f:
        text = remove_comment(f.read())
    if not text:
        return
    # 尝试运行
    try:
        if not preload:
            ast = parser.parse(text, debug=debug)
        else:
            ast = parser.parse(text)

        if show_tree and not preload:
            print(ast.get_tree())
        ast.exe()
    except:
        error_messages.insert(0, f'File `{path}`')
        print('\n\t'.join(error_messages))

# 错误的argument
def wrong_argument(msg):
    print(f'Wrong arguments: \033[1m{msg}\033[0m\n')
    help()

# 主函数
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

    # 预加载文件
    preload_scripts()

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

# 捕获 Keyboard Interrupt
def ctrl_c_handle(signal, frame):
    print(f'\nKeyboard Interrupt\n{preline} ', end='')

# 程序入口
if __name__ == '__main__':
    signal.signal(signal.SIGINT, ctrl_c_handle)

    lexer = lex.lex()
    parser = yacc.yacc()

    try:
        main()
    except EOFError:
        print("\nEXIT")
        sys.exit(0)
