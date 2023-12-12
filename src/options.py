import platform
from .update import VERSION, update, get_commit_hash_msg, get_current_branch
import os

PLATFORM = f'[ {platform.python_implementation()} {platform.python_version()} ] on {platform.system()}'

options_dict = {
    "show_tree": False,
    "show_parse": False,
    "show_time": False,
    "show_error": True
}

def _dict_connect(d: dict, space=4):
    max_left_size = max(len(i) for i in d.keys())
    result = []
    for left, right in d.items():
        result.append(left + ' '*(max_left_size-len(left)+space) + right)
    return result

def get_value(value):
    return options_dict[value]

def standard_output():
    print(f'CAIE Pseudocode Interpreter v{VERSION} ({get_current_branch()}/{get_commit_hash_msg()[0]})')
    print(f'Using {PLATFORM}')
    print('Repository at \033[4mhttps://github.com/iewnfod/CAIE_Code/\33[0m')
    print('Copyright (c) 2023 Iewnfod. ')
    print('All Rights Reserved. ')

def open_parse_info():
    options_dict['show_parse'] = True

def version():
    print(f'Version \033[1m{VERSION}\033[0m ({get_current_branch()}/{get_commit_hash_msg()[0]})')
    print(f'Using {PLATFORM}')
    print('Current Version Notes:', get_commit_hash_msg()[1])

def help():
    standard_output()

    print()

    print('Usage: \033[1mcpc\033[0m [file_paths] [options]')

    # 提示
    print('\033[2mThere should not be any space in a single file path. \nOr, you need to add double quotation marks around the path. \033[0m')

    print()

    print('Options:')
    arguments.sort()

    left_result = {}
    for i in arguments:
        left_result[f'    \033[1m{i.short_arg}\033[0m'] = f'\033[1m{i.long_arg}\033[0m'

    left_result = _dict_connect(left_result)
    result = {}
    for i in range(len(arguments)):
        result[left_result[i]] = arguments[i].description

    print('\n'.join(_dict_connect(result)))

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

def change_config(opt_name, value):
    from .global_var import set_config
    set_config(opt_name, value)

def migrate_files(directory):
    if os.path.isfile(directory):
        print('Please enter a dir path instead of a single file.')
        return
    for root, dirs, files in os.walk(directory):
        # Filter out directories starting with a dot
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.endswith('.p'):
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, file.replace('.p', '.cpc'))
                os.rename(old_file_path, new_file_path)

    print("Migration completed.")

def list_configs():
    from .global_var import config
    configs = sorted(config.config, key=lambda x : x[0])
    result = {}
    for key in configs:
        val = config.config[key]
        if val.name != key:
            left = f'{val.name}({key})'
        else:
            left = val.name

        result[left] = str(val.val)

    print('\n'.join(_dict_connect(result)))

def reset_configs():
    from .global_var import config
    config.reset_config()

def doc():
    from .history import HOME_PATH
    system = platform.system()
    file_path = os.path.join(HOME_PATH, 'Pseudocode Guide.pdf')
    if system == 'Windows':
        os.startfile(file_path)
    elif system == 'Linux':
        os.system(f'xdg-open "{file_path}"')
    elif system == 'Darwin':
        os.system(f'open "{file_path}"')

# 输入参数: (参数简写, 参数全称, 运行函数, 描述, 是否需要退出, 是否需要参数，参数数量，函数所需参数)
class Opt:
    def __init__(self, short_arg, long_arg, func, description, exit_program, value_num=0, *args, **kwargs):
        self.short_arg = short_arg
        self.long_arg = long_arg
        self.func = func
        self.description = description
        self.exit_program = exit_program
        self.value_num = value_num
        self.args = args
        self.kwargs = kwargs

    def check(self, t):
        return t == self.short_arg or t == self.long_arg

    def run(self, value):
        self.func(*value[1:self.value_num+1], *self.args, **self.kwargs)
        if self.exit_program:
            quit(0)

    def __lt__(self, other):
        if len(self.short_arg) == len(other.short_arg):
            return self.short_arg < other.short_arg
        else:
            return len(self.short_arg) < len(other.short_arg)


arguments = [
    Opt('-gt', '--get-tree', get_tree, 'To show the tree of the program after being parsed', False),
    Opt('-v', '--version', version, 'To show the version of this interpreter', True),
    Opt('-h', '--help', help, 'To show this help page', True),
    Opt('-p', '--parse', open_parse_info, 'To show parse information during running', False),
    Opt('-t', '--time', get_time, 'To show the time for the script to run', False),
    Opt('-k', '--keywords', show_keywords, 'To show all the keywords', True),
    Opt('-ne', '--no-error', remove_error, 'To remove all error messages', False),
    Opt('-u', '--update', update_version, 'To check or update the version (only if this is installed with git)', True),
    Opt('-c', '--config', change_config, 'To set configs of this interpreter', True, 2),
    Opt('-m', '--migrate', migrate_files, 'To migrate .p files to .cpc in a specified directory', True, 1),
    Opt('-lc', '--list-configs', list_configs, 'To list all the configs of the interpreter', True),
    Opt('-rc', '--reset-configs', reset_configs, 'To reset all the configs of the interpreter', True),
    Opt('-d', '--document', doc, 'To show the official document', True)
]
