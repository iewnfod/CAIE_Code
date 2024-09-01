from .global_var import *
from .AST_Base import *

reserved = {
    "CONSTANT",
    "DECLARE",
    "FOR",
    "TO",
    "STEP",
    "NEXT",
    "TYPE",
    "ENDTYPE",
    "INPUT",
    "OUTPUT",
    "IF",
    "THEN",
    "ELSE",
    "ENDIF",
    "CASE",
    "OF",
    "OTHERWISE",
    "ENDCASE",
    "REPEAT",
    "UNTIL",
    "WHILE",
    "DO",
    "ENDWHILE",
    "PROCEDURE",
    "ENDPROCEDURE",
    "CALL",
    "FUNCTION",
    "ENDFUNCTION",
    "PRIVATE",
    "PUBLIC",
    "AND",
    "OR",
    "NOT",
    "NEW",
    "CLASS",
    "INHERITS",
    "ENDCLASS",
    "ARRAY",
    "RETURNS",
    "RETURN",
    "OPENFILE",
    "READ",
    "WRITE",
    "APPEND",
    "READFILE",
    "WRITEFILE",
    "CLOSEFILE",
    "SEEK",
    "GETRECORD",
    "PUTRECORD",
    "RANDOM",
    "BYREF",
    "BYVAL",
    "MOD",
    "DIV",
    "DELETE",
    "PASS",
    "IMPORT",
    "SUPER",
    "SET",
    "DEFINE",
    "_OUTPUT",
}

tokens = (
    # 数据类型
    "INTEGER",
    "REAL",
    "CHAR",
    "STRING",
    "BOOLEAN",
    "DATE",
    # 算数运算
    "PLUS",
    "MINUS",
    "MUL",
    "N_DIV",
    # 符号
    "LEFT_PAREN", # (
    "RIGHT_PAREN", # )
    "LEFT_SQUARE", # [
    "RIGHT_SQUARE", # ]
    "LEFT_BRACE", # {
    "RIGHT_BRACE", # }
    "COLON", # :
    "COMMA", # ,
    "DOT", # .
    "POINTER", # ^
    "SEMICOLON", # ;
    "CONNECT", # &
    # 逻辑运算
    "LESS",
    "GREATER",
    "EQUAL",
    "LESS_EQUAL",
    "GREATER_EQUAL",
    "NOT_EQUAL",
    # 赋值
    "ASSIGN", # <-
    # Identifier
    "ID",
    # 换行
    "NEWLINE",
) + tuple(reserved)

# 匹配正则表达式
t_ASSIGN = r"(<-+)|←"
t_PLUS = r"\+"
t_MINUS = r"\-"
t_MUL = r"\*"
t_N_DIV = r"/"
t_LEFT_PAREN = r"\("
t_RIGHT_PAREN = r"\)"
t_LEFT_SQUARE = r"\["
t_RIGHT_SQUARE = r"\]"
t_LEFT_BRACE = r"\{"
t_RIGHT_BRACE = r"\}"
t_COLON = r":"
t_COMMA = r","
t_DOT = r"\."
t_LESS = r"<"
t_GREATER = r">"
t_EQUAL = r"="
t_LESS_EQUAL = r"<="
t_GREATER_EQUAL = r">="
t_NOT_EQUAL = r"<>"
t_POINTER = r"\^"
t_SEMICOLON = r";"
t_CONNECT = r"&"
# 忽视空格
t_ignore = r" "

# 规则行为
def t_DATE(t):
    r'[0-9][0-9]\/[0-9][0-9]\/[0-9][0-9][0-9][0-9]'
    t.value = str(t.value)
    return t

def t_BOOLEAN(t):
    r'TRUE|FALSE'
    if t.value == 'TRUE':
        t.value = True
    elif t.value == 'FALSE':
        t.value = False
    return t

def t_CHAR(t):
    r'\'[\s\S]?\''
    t.value = str(t.value[1:-1])
    return t

def t_STRING(t):
    r'\"[\s\S]*?\"'
    t.value = str(t.value[1:-1])
    return t

def t_REAL(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # 如果是关键字
    if t.value in reserved:
        t.type = t.value
    else:
        t.type = 'ID'
    return t

# 换行
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

# 意外处理
def t_error(t):
    add_lexer_error_message(f"Keyword not fount `{t.value[0]}`", AST_Node(lineno=t.lineno))
    t.lexer.skip(1)
