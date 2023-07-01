from src.error import Error
# 常量
default_value = {
    'INTEGER' : 0,
    'REAL' : 0.0,
    'CHAR' : '',
    'STRING' : "",
    'BOOLEAN' : True,
    'ARRAY': {},
}

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
