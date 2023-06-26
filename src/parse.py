import src.AST as AST

start = 'statements'

def p_error(p):
    if p:
        print(f'Parser Error: {p.value} at line {p.lineno}')
    else:
        print(f'Syntax Error: EOF')

def p_statements(p):
    """statements : statements statement
            | statement"""
    if len(p) == 2:
        p[0] = AST.Statements()
        p[0].add_statement(p[1])
    else:
        p[1].add_statement(p[2])
        p[0] = p[1]

def p_declare_statement(p):
    """statement : DECLARE ID COLON ID"""
    p[0] = AST.Variable(p[2], p[4])

def p_const_declare_statement(p):
    """statement : CONSTANT ID EQUAL expression"""

def p_array_declare_statement(p):
    """statement : DECLARE ID COLON ARRAY LEFT_SQUARE dimensions RIGHT_SQUARE OF ID
        dimensions : dimensions COMMA dimension
            | dimension
        dimension : expression COLON expression"""

def p_assign_statement(p):
    """statement : ID ASSIGN expression"""
    p[0] = AST.Assign(p[1], p[3])

def p_array_assign_statement(p):
    "statement : ID LEFT_SQUARE indexes RIGHT_SQUARE ASSIGN expression"

def p_indexes(p):
    """indexes : indexes COMMA expression
            | expression
            | expression TO expression"""

def p_input_statement(p):
    """statement : INPUT ID"""
    p[0] = AST.Input(p[2])

def p_OUTPUT_statement(p):
    """statement : OUTPUT expression"""
    p[0] = AST.Output(p[2])

def p_if_statement(p):
    """statement : IF expression THEN statements ENDIF
            | IF expression THEN statements ELSE statements ENDIF"""
    print('if statement')

def p_case_statement(p):
    """statement : CASE OF ID cases ENDCASE"""
    print('case statement')

def p_cases(p):
    """cases : cases case
            | case

        case : indexes COLON statements
            | OTHERWISE COLON statements"""

def p_for_statement(p):
    """statement : FOR ID ASSIGN expression TO expression statements NEXT ID"""
    print('for statement')

def p_repeat_statement(p):
    """statement : REPEAT statements UNTIL expression"""

def p_while_statement(p):
    """statement : WHILE expression statements ENDWHILE"""

def p_expression_statement(p):
    """statement : expression"""

def p_id_expression(p):
    """expression : ID"""
    p[0] = AST.Get(p[1])

def p_or_expression(p):
    """expression : expression OR expression"""

def p_and_expression(p):
    """expression : expression AND expression"""

def p_not_expression(p):
    """expression : NOT expression"""

def p_equal_expression(p):
    """expression : expression EQUAL expression"""

def p_not_equal_expression(p):
    """expression : expression NOT_EQUAL expression"""

def p_less_expression(p):
    """expression : expression LESS expression"""

def p_greater_expression(p):
    """expression : expression GREATER expression"""

def p_less_equal_expression(p):
    """expression : expression LESS_EQUAL expression"""

def p_greater_equal_expression(p):
    """expression : expression GREATER_EQUAL expression"""

def p_mul_expression(p):
    """expression : expression MUL expression"""

def p_div_expression(p):
    """expression : expression DIV expression"""

def p_plus_expression(p):
    """expression : expression PLUS expression"""

def p_minus_expression(p):
    """expression : expression MINUS expression"""

# 匹配基础数据类型
def p_char_expression(p):
    """expression : CHAR"""

def p_string_expression(p):
    """expression : STRING"""

def p_real_expression(p):
    """expression : REAL"""

def p_int_expression(p):
    """expression : INTEGER"""
    p[0] = AST.Integer(p[1])
