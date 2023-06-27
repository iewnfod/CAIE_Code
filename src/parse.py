import src.AST as AST

start = 'statements'

def p_error(p):
    if p:
        print(f'Parser Error: `{p.value}` at line {p.lineno}')
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
    p[0] = AST.Constant(p[2], p[4])

def p_array_declare_statement(p):
    """statement : DECLARE ID COLON ARRAY LEFT_SQUARE dimensions RIGHT_SQUARE OF ID"""
    p[0] = AST.Array(p[2], p[6], p[9])

def p_dimensions_expression(p):
    """dimensions : dimensions COMMA dimension
        | dimension"""
    if len(p) == 2:
        p[0] = AST.Dimensions()
        p[0].add_dimension(p[1])
    else:
        p[1].add_dimension(p[3])
        p[0] = p[1]

def p_dimension_expression(p):
    """dimension : expression COLON expression"""
    p[0] = AST.Dimension(p[1], p[3])

def p_assign_statement(p):
    """statement : ID ASSIGN expression"""
    p[0] = AST.Assign(p[1], p[3])

def p_array_assign_statement(p):
    "statement : ID LEFT_SQUARE indexes RIGHT_SQUARE ASSIGN expression"
    p[0] = AST.Array_assign(p[1], p[3], p[6])

def p_indexes(p):
    """indexes : indexes COMMA expression
            | expression"""
    if len(p) == 2:
        p[0] = AST.Indexes()
        p[0].add_index(p[1])
    else:
        p[1].add_index(p[3])
        p[0] = p[1]

def p_input_statement(p):
    """statement : INPUT ID"""
    p[0] = AST.Input(p[2])

def p_array_input(p):
    """statement : INPUT ID LEFT_SQUARE indexes RIGHT_SQUARE"""
    p[0] = AST.Array_input(p[2], p[4])

def p_output_statement(p):
    """statement : OUTPUT output_expression"""
    p[0] = AST.Output(p[2])

def p_output_expression(p):
    """output_expression : output_expression COMMA expression
            | expression"""
    if len(p) == 2:
        p[0] = AST.Output_expression()
        p[0].add_expression(p[1])
    else:
        p[1].add_expression(p[3])
        p[0] = p[1]

def p_if_statement(p):
    """statement : IF expression THEN statements ELSE statements ENDIF
            | IF expression THEN statements ENDIF"""
    if len(p) == 6:
        p[0] = AST.If(p[2], p[4])
    else:
        p[0] = AST.If(p[2], p[4], p[6])

def p_case_statement(p):
    """statement : CASE OF ID cases ENDCASE"""

def p_cases(p):
    """cases : cases case
            | case

        case : indexes COLON statements
            | OTHERWISE COLON statements"""

def p_for_statement(p):
    """statement : FOR ID ASSIGN expression TO expression statements NEXT ID"""


def p_repeat_statement(p):
    """statement : REPEAT statements UNTIL expression"""

def p_while_statement(p):
    """statement : WHILE expression statements ENDWHILE"""

def p_expression_statement(p):
    """statement : expression"""
    p[0] = AST.Output(p[1])

def p_id_expression(p):
    """expression : ID"""
    p[0] = AST.Get(p[1])

def p_array_id_expression(p):
    """expression : ID LEFT_SQUARE indexes RIGHT_SQUARE"""
    p[0] = AST.Array_get(p[1], p[3])

def p_or_expression(p):
    """expression : expression OR expression"""
    p[0] = AST.Logic_or(p[1], p[3])

def p_and_expression(p):
    """expression : expression AND expression"""
    p[0] = AST.Logic_and(p[1], p[3])

def p_not_expression(p):
    """expression : NOT expression"""
    p[0] = AST.Logic_not(p[2])

def p_equal_expression(p):
    """expression : expression EQUAL expression"""
    p[0] = AST.Cmp_equal(p[1], p[3])

def p_not_equal_expression(p):
    """expression : expression NOT_EQUAL expression"""
    p[0] = AST.Cmp_not_equal(p[1], p[3])

def p_less_expression(p):
    """expression : expression LESS expression"""
    p[0] = AST.Cmp_less(p[1], p[3])

def p_greater_expression(p):
    """expression : expression GREATER expression"""
    p[0] = AST.Cmp_greater(p[1], p[3])

def p_less_equal_expression(p):
    """expression : expression LESS_EQUAL expression"""
    p[0] = AST.Cmp_less_equal(p[1], p[3])

def p_greater_equal_expression(p):
    """expression : expression GREATER_EQUAL expression"""
    p[0] = AST.Cmp_greater_equal(p[1], p[3])

def p_mul_expression(p):
    """expression : expression MUL expression"""
    p[0] = AST.Op_mul(p[1], p[3])

def p_div_expression(p):
    """expression : expression DIV expression"""
    p[0] = AST.Op_div(p[1], p[3])

def p_plus_expression(p):
    """expression : expression PLUS expression"""
    p[0] = AST.Op_plus(p[1], p[3])

def p_minus_expression(p):
    """expression : expression MINUS expression"""
    p[0] = AST.Op_minus(p[1], p[3])

# 括号
def p_paren_expression(p):
    """expression : LEFT_PAREN expression RIGHT_PAREN"""
    p[0] = p[2]

# 匹配基础数据类型
def p_boolean_expression(p):
    """expression : BOOLEAN"""
    p[0] = AST.Boolean(p[1])

def p_char_expression(p):
    """expression : CHAR"""
    p[0] = AST.Char(p[1])

def p_string_expression(p):
    """expression : STRING"""
    p[0] = AST.String(p[1])

def p_real_expression(p):
    """expression : REAL"""
    p[0] = AST.Real(p[1])

def p_int_expression(p):
    """expression : INTEGER"""
    p[0] = AST.Integer(p[1])
