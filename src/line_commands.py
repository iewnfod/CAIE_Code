from .quit import quit
from .options import help
from os import get_terminal_size

def clear():
    size = get_terminal_size()
    print('\n'*(size.lines+1))

commands = {
    'exit': quit,
    'help': help,
    'clear': clear
}

def run_command(text: str):
    text = text.lower()
    if text in commands:
        commands[text]()
        return True
    else:
        return False
