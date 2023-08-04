from src.lex import *
from src.parse import *
import src.options as options
import src.global_var as global_var
from ply import yacc
from ply import lex
from sys import argv, exit
import os
from chardet import detect
from time import time
# 尝试导入 readline，无法导入也不会导致核心功能受损
try:
    import readline
    readline.clear_history()
except:
    pass

preline = '>'
multi_preline = '.'

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
    l = list(set(global_var.get_error_messages()))
    l.reverse()
    if l:
        # 输出文件路径
        if p:
            print(f'File `{p}`: ')
        # 输出错误信息
        for i in l:
            i.raise_err()
        # 清空错误数组
        global_var.clear_error_messages()

# 多行输入
def multi_input():
    text = remove_comment(input(f'{preline} '))
    # 若为空，那就直接返回
    if not text:
        return ''
    # 尝试解析
    try:
        parser.parse(text)
    except Exception as e:
        add_error_message(str(e), AST_Node())
    # 空了 n 行
    n = 0
    # 如果出现了错误信息，那就说明这一行没写完，那就换行再写
    while get_error_messages() and n < 2:
        clear_error_messages()
        t = remove_comment(input(f'{multi_preline} '))
        # 如果这一行还是空，那就给一次机会，否则就视为结束，然后开始运行
        if not t:
            n += 1
        else:
            n = 0
        # 加上新的一行
        text += '\n' + t
        # 再尝试解析
        try:
            parser.parse(text)
        except Exception as e:
            add_error_message(str(e), AST_Node())

    return text

# 运行 AST
def run_AST(ast, preload=False):
    if options.show_tree and not preload:
        print(ast.get_tree())

    if options.show_time and not preload:
        t = time()

    ast.exe()

    if options.show_time and not preload:
        t = time() - t
        print(f'\033[4mDuration: {t}s\033[0m')


# 终端模式，逐行输入并解析运行
def with_line():
    # 基准输出
    options.standard_output()
    # 运行
    while 1:
        text = multi_input()
        lexer.lineno = 1
        if not text:
            continue
        try:
            ast = parser.parse(text, debug=options.parse)

            run_AST(ast)

        except:
            pass

        output_error()

# 文件模式，读取文件并解析运行
def with_file(path, preload=False):
    # 恢复行数，也就是不计算预加载文件的行数
    lexer.lineno = 1
    # 读取文件编码
    with open(path, 'rb') as f:
        encode = detect(f.read())['encoding']
    # 读取文件
    with open(path, 'r', encoding=encode) as f:
        text = remove_comment(f.read())
    if not text:
        return

    # 尝试运行
    try:
        if not preload:
            ast = parser.parse(text, debug=options.parse)
        else:
            ast = parser.parse(text)

        run_AST(ast, preload=preload)

    except:
        pass

    output_error(path)

# 错误的argument
def wrong_argument(msg):
    print(f'Wrong arguments: \033[1m{msg}\033[0m\n')
    options.help()

# 主函数
def main():
    # 解析参数
    file_path = ''
    for arg in argv[1:]:
        for i in options.arguments:
            if arg == i[0] or arg == i[1]:
                i[2]()
                break
        else:
            if arg[0] == '-':
                wrong_argument(f'Unknown option {arg}')
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
            wrong_argument(f'File `{file_path}` does not exist')


# 程序入口
if __name__ == '__main__':
    global_var.__init__()

    lexer = lex.lex()
    parser = yacc.yacc()

    try:
        main()
    except EOFError:
        print("\nEXIT")
        exit(0)
    except KeyboardInterrupt:
        print('\nKeyboard Interrupt')
        exit(0)
