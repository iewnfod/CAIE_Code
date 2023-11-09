import os
import time
import threading

flags = {}


def animation(msg, count):
    n = 0
    while flags[msg]:
        n += 1
        print(msg + '.' * n + ' ' * (count - n), end='\r')
        n %= count
        time.sleep(.5)


def new_animation(msg: str, count: int, work, failed_msg='', *args, **kwargs):
    flags[msg] = True
    threading.Thread(target=animation, args=(msg, count)).start()
    try:
        result = work(*args, **kwargs)
    except Exception as e:
        print(f'\033[1;31m{failed_msg}\033[0m\n{e}')
        os._exit(1)
    flags[msg] = False
    return result
