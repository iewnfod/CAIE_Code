from sys import exit
import platform
from .update import VERSION, update

PLATFORM = f'[ {platform.python_implementation()} {platform.python_version()} ] on {platform.system()}'

options_dict = {
    "show_tree": False,
    "show_parse": False,
    "show_time": False,
    "show_error": True
}
show_error = True

def get_value(value):
    return options_dict[value]

def standard_output():
    print(f'CAIE Pseudocode Interpreter v{VERSION}')
    print(f'Using {PLATFORM}')
    print('Repository at \033[4mhttps://github.com/iewnfod/CAIE_Code/\33[0m')
    print('Copyright (c) 2023 Iewnfod. ')
    print('All Rights Reserved. ')

def open_parse_info():
    options_dict['show_parse'] = True

def version():
    print(f'Version: \033[1m{VERSION}\033[0m')
    exit(0)

def help():
    standard_output()

    print()

    print('Usage: \033[1mcpc\033[0m [file_path] [options]')

    # 提示
    print('\033[2mThere should not be any space in a file path. \nOr, you need to add double quotation marks around the path. \033[0m')

    print()

    print('Options:')
    arguments.sort()
    for i in arguments:
        print('\t\033[1m', i.short_arg, '\t', i.long_arg, '\033[0m\t', i.description)

def get_tree():
    options_dict['show_tree'] = True

def get_time():
    options_dict['show_time'] = True

def show_keywords():
    from src.lex import reserved
    keywords = sorted(reserved)
    l = {}
    for k in keywords:
        if k[0] in l.keys():
            l[k[0]].append(k)
        else:
            l[k[0]] = [k]

    print('Keywords:')
    for v in l.values():
        for k in v:
            print(f'\033[1m{k}\033[0m', end=' ')
        print()

def remove_error():
    options_dict['show_error'] = False

def update_version():
    update()


# 输入参数: (参数简写, 参数全称, 运行函数, 描述, 是否需要退出, 函数所需参数)
class Opt:
    def __init__(self, short_arg, long_arg, func, description, exit_program, *args, **kwargs):
        self.short_arg = short_arg
        self.long_arg = long_arg
        self.func = func
        self.description = description
        self.exit_program = exit_program
        self.args = args
        self.kwargs = kwargs

    def check(self, t):
        return t == self.short_arg or t == self.long_arg

    def run(self):
        self.func(*self.args, **self.kwargs)
        if self.exit_program:
            quit(0)

    def __lt__(self, other):
        return self.short_arg < other.short_arg


arguments = [
    Opt('-gt', '--get-tree', get_tree, 'To show the tree of the program after being parsed', False),
    Opt('-v', '--version', version, 'To show the version of this interpreter', True),
    Opt('-h', '--help', help, 'To show this help page', True),
    Opt('-p', '--parse', open_parse_info, 'To show parse information during running', False),
    Opt('-t', '--time', get_time, 'To show the time for the script to run', False),
    Opt('-k', '--keywords', show_keywords, 'To show all the keywords', True),
    Opt('-ne', '--no-error', remove_error, 'To remove all error messages', False),
    Opt('-u', '--update', update_version, 'To check or update the version (only if this is installed with git)', True),
]
