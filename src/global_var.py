from src.error import Error

# 变量
def __init__():
    global error_messages
    error_messages = []

def add_error_message(msg, obj):
    error_messages.append(Error(msg, obj))

def get_error_messages():
    return error_messages

def clear_error_messages():
    global error_messages
    error_messages = []
