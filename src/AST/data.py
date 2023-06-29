from src.stack import Stack

LEVEL_STR = '| '
stack = Stack()

def check_type_equal(t1, t2):
    if t1 == t2:
        return True
    if (t1 == 'INTEGER' and t2 == 'REAL') or (t1 == 'REAL' and t2 == 'INTEGER'):
        return True
    return False
