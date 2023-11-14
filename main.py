# 检查依赖
from src.requirements import test_requirements
test_requirements()
# 依赖库导入
from ply import yacc
from ply import lex
from chardet import detect
# 导入色彩基础库，保证\033能正确的转译
import colorama
colorama.init()

# 全局变量初始化
import src.global_var as global_var

# 正式导入
from src.lex import *
from src.parse import *
import src.options as options
from src.history import HOME_PATH
from src.quit import quit
from src.line_commands import run_command
from src.update import update

import sys
import os
from time import time


preline = '>'
multi_preline = '.'
home_path = HOME_PATH


# 错误的argument
def wrong_argument(msg):
    print(f'Unknown argument: {msg}')
    print(f'Use `cpc -h` to get detailed informations about how to use')
    quit(1)
    # options.help()

# 清除注释以及多余字符
def remove_comment(text: str):
    text = text.split('\n')
    for i in range(len(text)):
        text[i] = text[i].split('//')[0].strip()

    return '\n'.join(text).strip()

# 预加载文件
def preload_scripts():
    scripts_path = os.path.join(home_path, 'scripts')
    for p, _dir_list, file_list in os.walk(scripts_path):
        for i in file_list:
            path = os.path.join(p, i)
            _, n = os.path.splitext(path)
            if n == '.cpc':
                with_file(path, True)

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
    while not is_error_messages_empty() and n < 2:
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
    if options.get_value('show_tree') and not preload:
        print(ast.get_tree())

    if options.get_value('show_time') and not preload:
        t = time()

    ast.exe()

    if options.get_value('show_time') and not preload:
        t = time() - t
        print(f'\033[4mDuration: {t}s\033[0m')


# 终端模式，逐行输入并解析运行
def with_line():
    global_var.set_running_mod('line')
    global_var.set_running_path('')
    # 基准输出
    options.standard_output()
    # 运行
    while 1:
        text = multi_input()
        lexer.lineno = 1
        # 尝试运行特殊指令
        if run_command(text):
            continue

        if not text:
            continue
        try:
            ast = parser.parse(text, debug=options.get_value('show_parse'))

            run_AST(ast)

        except:
            pass

        global_var.output_error()

# 文件模式，读取文件并解析运行
def with_file(path, preload=False):
    global_var.set_running_mod('file')
    global_var.set_running_path(path)
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
            ast = parser.parse(text, debug=options.get_value('show_parse'))
        else:
            ast = parser.parse(text)

        run_AST(ast, preload=preload)

    except:
        pass

    global_var.output_error()

# 主函数
def main(input_=None, output_=None, addition_file_name=None):
    # 设置输入输出
    if input_: global_var.set_std_in(input_)
    if output_: global_var.set_std_out(output_)

    # 解析参数
    argv = sys.argv
    file_paths = set()
    i = 1
    while i < len(argv):
        arg = argv[i]
        for opt in options.arguments:
            if opt.check(arg):
                opt.run(argv[i:])
                i += opt.value_num
                break
        else:
            if arg[0] == '-':
                wrong_argument(f'Unknown option `{arg}`')
            else:
                file_paths.add(arg)
        i += 1

    if addition_file_name:
        file_paths.add(addition_file_name)

    #自动更新
    if config.get_config('dev.simulate-update') or (config.get_config('auto-update') and not config.get_config('dev') and update.update_expired()):
        update()
        config.set_config('last-auto-check', time())
    
    # 预加载文件
    preload_scripts()

    # 选择模式运行
    if not file_paths:
        with_line()
    else:
        for file_path in file_paths:
            lexer.lineno = 1
            # 选择模式运行
            if os.path.exists(file_path):
                if os.path.isfile(file_path):
                    with_file(file_path)
                else:
                    wrong_argument(f'`{file_path}` is not a file')
            else:
                wrong_argument(f'File `{file_path}` does not exist')

# 加载基础类型
global_var.__init__()

lexer = lex.lex()
parser = yacc.yacc()

# 程序入口
if __name__ == '__main__':
    try:
        main()
    except EOFError:
        print("EXIT")
        quit(0)
    except KeyboardInterrupt:
        print('Keyboard Interrupt')
        quit(0)
    except Exception as e:
        print(e)
        quit(1)
