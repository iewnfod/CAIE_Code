from src.lex import *
from src.parse import *
import src.options as options
import src.global_var as global_var
from ply import yacc
from ply import lex
import sys
import os
import chardet
import time
# 尝试导入 readline，无法导入也不会导致核心功能受损
try:
    import readline
    readline.clear_history()
except:
    pass

preline = '$'

# 清除注释以及多余字符
def remove_comment(text):
    text = text.split('\n')
    for i in range(len(text)):
        text[i] = text[i].split('//')[0]

    return '\n'.join(text).strip()

# 预加载文件
def preload_scripts():
    scripts_path = os.path.join(os.path.dirname(__file__), 'scripts')
    for p, dir_list, file_list in os.walk(scripts_path):
        for i in file_list:
            path = os.path.join(p, i)
            _, n = os.path.splitext(path)
            if n == '.cpc':
                with_file(path, True)

# 输出错误信息
def output_error(p=''):
    l = global_var.get_error_messages()
    if l:
        # 输出文件路径
        if p:
            print(f'File `{p}`: ')
        # 输出错误信息
        for i in l:
            i.raise_err()
        # 清空错误数组
        global_var.clear_error_messages()

# 终端模式，逐行输入并解析运行
def with_line():
    # 基准输出
    options.standard_output()
    # 运行
    while 1:
        text = remove_comment(input(f'{preline} '))
        if not text:
            continue
        try:
            ast = parser.parse(text, debug=options.debug)
            if options.show_tree:
                print(ast.get_tree())

            if options.show_time:
                t = time.time()

            ast.exe()

            if options.show_time:
                t = time.time() - t
                print(f'\033[4mDuration: {t}s\033[0m')

        except:
            pass

        output_error()

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
            ast = parser.parse(text, debug=options.debug)
        else:
            ast = parser.parse(text)

        if options.show_tree and not preload:
            print(ast.get_tree())


        if options.show_time and not preload:
            t = time.time()

        ast.exe()

        if options.show_time and not preload:
            t = time.time() - t
            print(f'\033[4mDuration: {t}s\033[0m')

    except:
        pass

    output_error(path)

# 错误的argument
def wrong_argument(msg):
    print(f'Wrong arguments: \033[1m{msg}\033[0m\n')
    help()

# 主函数
def main():
    # 解析参数
    file_path = ''
    for arg in sys.argv[1:]:
        for i in options.arguments:
            if arg == i[0] or arg == i[1]:
                i[2]()
                break
        else:
            file_path = arg

    # 预加载文件
    preload_scripts()

    lexer.lineno = 1
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


# 程序入口
if __name__ == '__main__':
    global_var.__init__()

    lexer = lex.lex()
    parser = yacc.yacc()

    try:
        main()
    except EOFError:
        print("\nEXIT")
        sys.exit(0)
    except KeyboardInterrupt:
        print('\nKeyboard Interrupt')
        sys.exit(0)
