from .quit import quit
from .options import help, update_version
from os import get_terminal_size


def clear():
    size = get_terminal_size()
    print('\n' * (size.lines + 1))


commands = {
    'exit': quit,
    'help': help,
    'clear': clear,
    'update': update_version
}


def run_command(text: str):
    text = text.lower()
    if text in commands:
        commands[text]()
        return True
    else:
        return False
