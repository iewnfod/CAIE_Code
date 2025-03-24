from . import AST
from .AST.insert_func import *
from .global_var import *
from .error import *
from .AST_Base import *

start = 'statements'

# 符号优先级
# 越往下优先级越高
precedence = (
    # 逻辑运算
    ("left", "AND"),
    ("left", "OR"),
    ("left", "NOT"),
    # 比较运算
    ("left", "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", "EQUAL", "NOT_EQUAL"),
    # 加减乘除
    ("left", "PLUS", "MINUS"),
    ("left", "MUL", "N_DIV", "MOD", "DIV"),
    # 右结合操作符
    ("right", "UMINUS"),
    ("right", "UPLUS"),
)


def p_error(p):
    if p:
        add_parse_error_message(f'{p.type} `{p.value}`', AST_Node(p=p))
    else:
        add_eof_error_message(AST_Node())

def p_statements(p):
    """statements : statements statement
            | statement"""
    if len(p) == 2:
        p[0] = AST.Statements(p=p)
        p[0].add_statement(p[1])
    else:
        p[1].add_statement(p[2])
        p[0] = p[1]

def p_delete_statement(p):
    """statement : DELETE ID"""
    p[0] = AST.Delete(p[2], p=p)

def p_declare_statement(p):
    """statement : DECLARE ID COLON ID
            | PUBLIC ID COLON ID"""
    p[0] = AST.Variable(p[2], p[4], p=p)

def p_multi_declare_statement(p):
    """statement : DECLARE ids COLON ID
            | PUBLIC ids COLON ID"""
    p[0] = AST.MultiVariables(p[2], p[4], p=p)

def p_multi_id_expression(p):
    """ids : ids COMMA ID
        | ID"""
    if len(p) == 2:
        p[0] = AST.Ids(p=p)
        p[0].add_id(p[1])
    else:
        p[1].add_id(p[3])
        p[0] = p[1]

def p_private_declare_statement(p):
    """statement : PRIVATE ID COLON ID"""
    p[0] = AST.Variable(p[2], p[4], private=True, p=p)

def p_private_multi_declare_statement(p):
    """statement : PRIVATE ids COLON ID"""
    p[0] = AST.MultiVariables(p[2], p[4], private=True, p=p)

def p_const_declare_statement(p):
    """statement : CONSTANT ID EQUAL expression
            | CONSTANT ID ASSIGN expression"""
    p[0] = AST.Constant(p[2], p[4], p=p)

def p_array_declare_statement(p):
    """statement : DECLARE ID COLON ARRAY LEFT_SQUARE dimensions RIGHT_SQUARE OF ID
            | PUBLIC ID COLON ARRAY LEFT_SQUARE dimensions RIGHT_SQUARE OF ID"""
    p[0] = AST.Array(p[2], p[6], p[9], p=p)

def p_private_array_declare_statement(p):
    """statement : PRIVATE ID COLON ARRAY LEFT_SQUARE dimensions RIGHT_SQUARE OF ID"""
    p[0] = AST.Array(p[2], p[6], p[9], private=True, p=p)

def p_dimensions_expression(p):
    """dimensions : dimensions COMMA dimension
        | dimension"""
    if len(p) == 2:
        p[0] = AST.Dimensions(p=p)
        p[0].add_dimension(p[1])
    else:
        p[1].add_dimension(p[3])
        p[0] = p[1]

def p_dimension_expression(p):
    """dimension : expression COLON expression"""
    p[0] = AST.Dimension(p[1], p[3], p=p)

# def p_assign_statement(p):
#     """statement : ID ASSIGN expression"""
#     p[0] = AST.Assign(p[1], p[3], p=p)

# def p_array_assign_statement(p):
#     """statement : ID LEFT_SQUARE indexes RIGHT_SQUARE ASSIGN expression"""
#     p[0] = AST.Array_assign(p[1], p[3], p[6], p=p)

def p_new_assign_statement(p):
    """statement : expression ASSIGN expression"""
    p[0] = AST.NewAssign(p[1], p[3], p=p)

def p_indexes(p):
    """indexes : indexes COMMA expression
            | expression"""
    if len(p) == 2:
        p[0] = AST.Indexes(p=p)
        p[0].add_index(p[1])
    else:
        p[1].add_index(p[3])
        p[0] = p[1]

def p_array_expression(p):
    """expression : LEFT_SQUARE array_items RIGHT_SQUARE
            | LEFT_SQUARE RIGHT_SQUARE"""
    if len(p) == 4:
        p[0] = AST.Array_expression(p[2], p=p)
    else:
        p[0] = AST.Array_expression(AST.Array_items(p=p), p=p)

def p_array_items(p):
    """array_items : array_items COMMA expression
            | expression"""
    if len(p) == 2:
        p[0] = AST.Array_items(p=p)
        p[0].add_item(p[1])
    else:
        p[1].add_item(p[3])
        p[0] = p[1]

# def p_input_statement(p):
#     """statement : INPUT ID"""
#     p[0] = AST.Input(p[2], p=p)

# def p_array_input(p):
#     """statement : INPUT ID LEFT_SQUARE indexes RIGHT_SQUARE"""
#     p[0] = AST.Array_input(p[2], p[4], p=p)

def p_new_input_statement(p):
    """statement : INPUT expression"""
    p[0] = AST.NewInput(p[2], p=p)

def p_output_statement(p):
    """statement : OUTPUT output_expression"""
    p[0] = AST.Output(p[2], p=p)

def p_no_end_output_statement(p):
    """statement : _OUTPUT output_expression"""
    p[0] = AST.Output(p[2], end="", p=p)

def p_output_expression(p):
    """output_expression : output_expression COMMA expression
            | expression"""
    if len(p) == 2:
        p[0] = AST.Output_expression(p=p)
        p[0].add_expression(p[1])
    else:
        p[1].add_expression(p[3])
        p[0] = p[1]

def p_if_statement(p):
    """statement : IF expression THEN statements ELSE statements ENDIF
            | IF expression THEN statements ENDIF"""
    if len(p) == 6:
        p[0] = AST.If(p[2], p[4], p=p)
    else:
        p[0] = AST.If(p[2], p[4], p[6], p=p)

# def p_case_statement(p):
#     """statement : CASE OF ID cases ENDCASE"""
#     p[0] = AST.Case(p[3], p[4], p=p)

# def p_case_array_statement(p):
#     """statement : CASE OF ID LEFT_SQUARE indexes RIGHT_SQUARE cases ENDCASE"""
#     p[0] = AST.Case_array(p[3], p[5], p[7], p=p)

def p_new_case_statement(p):
    """statement : CASE OF expression cases ENDCASE"""
    p[0] = AST.NewCase(p[3], p[4], p=p)

def p_cases(p):
    """cases : cases case
            | case"""
    if len(p) == 2:
        p[0] = AST.Cases(p=p)
        p[0].add_case(p[1])
    else:
        p[1].add_case(p[2])
        p[0] = p[1]

def p_case(p):
    """case : case_expression COLON statements SEMICOLON
            | otherwise_statement SEMICOLON"""
    if len(p) == 3:
        p[0] = p[1]
    else:
        p[0] = AST.A_case(p[1], p[3], p=p)

def p_case_expression(p):
    """case_expression : expression TO expression
            | expression"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = AST.Range(p[1], p[3], p=p)

def p_otherwise_statement(p):
    """otherwise_statement : OTHERWISE COLON statements"""
    p[0] = AST.A_case(None, p[3], True, p=p)

def p_for_statement(p):
    """statement : FOR ID ASSIGN expression TO expression STEP expression statements NEXT ID
            | FOR ID ASSIGN expression TO expression statements NEXT ID"""
    if len(p) == 10:
        p[0] = AST.For(p[2], p[4], p[6], AST.Integer(1, p=p), p[7], p[9], p=p)
    else:
        p[0] = AST.For(p[2], p[4], p[6], p[8], p[9], p[11], p=p)

def p_repeat_statement(p):
    """statement : REPEAT statements UNTIL expression"""
    p[0] = AST.Repeat(p[2], p[4], p=p)

def p_while_statement(p):
    """statement : WHILE expression DO statements ENDWHILE
            | WHILE expression statements ENDWHILE"""
    if len(p) == 5:
        p[0] = AST.While(p[2], p[3], p=p)
    else:
        p[0] = AST.While(p[2], p[4], p=p)

def p_expression_statement(p):
    """statement : expression"""
    p[0] = AST.Raw_output(p[1], p=p)

def p_id_expression(p):
    """expression : ID"""
    p[0] = AST.Get(p[1], p=p)

def p_array_id_expression(p):
    """expression : ID LEFT_SQUARE indexes RIGHT_SQUARE"""
    p[0] = AST.Array_get(p[1], p[3], p=p)

def p_or_expression(p):
    """expression : expression OR expression"""
    p[0] = AST.Logic_or(p[1], p[3], p=p)

def p_and_expression(p):
    """expression : expression AND expression"""
    p[0] = AST.Logic_and(p[1], p[3], p=p)

def p_not_expression(p):
    """expression : NOT expression"""
    p[0] = AST.Logic_not(p[2], p=p)

def p_equal_expression(p):
    """expression : expression EQUAL expression"""
    p[0] = AST.Cmp_equal(p[1], p[3], p=p)

def p_not_equal_expression(p):
    """expression : expression NOT_EQUAL expression"""
    p[0] = AST.Cmp_not_equal(p[1], p[3], p=p)

def p_less_expression(p):
    """expression : expression LESS expression"""
    p[0] = AST.Cmp_less(p[1], p[3], p=p)

def p_greater_expression(p):
    """expression : expression GREATER expression"""
    p[0] = AST.Cmp_greater(p[1], p[3], p=p)

def p_less_equal_expression(p):
    """expression : expression LESS_EQUAL expression"""
    p[0] = AST.Cmp_less_equal(p[1], p[3], p=p)

def p_greater_equal_expression(p):
    """expression : expression GREATER_EQUAL expression"""
    p[0] = AST.Cmp_greater_equal(p[1], p[3], p=p)

def p_mod_expression(p):
    """expression : expression MOD expression"""
    p[0] = AST.Op_mod(p[1], p[3], p=p)

def p_exact_div_expression(p):
    """expression : expression DIV expression"""
    p[0] = AST.Op_exact_div(p[1], p[3], p=p)

def p_mul_expression(p):
    """expression : expression MUL expression"""
    p[0] = AST.Op_mul(p[1], p[3], p=p)

def p_div_expression(p):
    """expression : expression N_DIV expression"""
    p[0] = AST.Op_div(p[1], p[3], p=p)

def p_uminus_expression(p):
    """expression : MINUS expression %prec UMINUS"""
    p[0] = AST.Op_minus(AST.Integer(0, p=p), p[2], p=p)

def p_uplus_expression(p):
    """expression : PLUS expression %prec UPLUS"""
    p[0] = AST.Op_plus(AST.Integer(0, p=p), p[2], p=p)

def p_plus_expression(p):
    """expression : expression PLUS expression"""
    p[0] = AST.Op_plus(p[1], p[3], p=p)

def p_minus_expression(p):
    """expression : expression MINUS expression"""
    p[0] = AST.Op_minus(p[1], p[3], p=p)

def p_connect_expression(p):
    """expression : expression CONNECT expression"""
    p[0] = AST.Op_connect(p[1], p[3], p=p)

# 括号
def p_paren_expression(p):
    """expression : LEFT_PAREN expression RIGHT_PAREN"""
    p[0] = p[2]

# 匹配基础数据类型
def p_date_expression(p):
    """expression : DATE"""
    p[0] = AST.Date(p[1], p=p)

def p_boolean_expression(p):
    """expression : BOOLEAN"""
    p[0] = AST.Boolean(p[1], p=p)

def p_char_expression(p):
    """expression : CHAR"""
    p[0] = AST.Char(p[1], p=p)

def p_string_expression(p):
    """expression : STRING"""
    p[0] = AST.String(p[1], p=p)

def p_real_expression(p):
    """expression : REAL"""
    p[0] = AST.Real(p[1], p=p)

def p_int_expression(p):
    """expression : INTEGER"""
    p[0] = AST.Integer(p[1], p=p)


# 函数的声明与调用
def p_declare_parameters(p):
    """declare_parameters : declare_parameters COMMA declare_parameter
            | declare_parameter"""
    if len(p) == 2:
        p[0] = AST.Declare_parameters(p=p)
        p[0].add_parameter(p[1])
    else:
        p[1].add_parameter(p[3])
        p[0] = p[1]

def p_declare_parameter(p):
    """declare_parameter : ID COLON ID
            | ID COLON ARRAY
            | BYREF ID COLON ID
            | BYREF ID COLON ARRAY
            | BYVAL ID COLON ID
            | BYVAL ID COLON ARRAY"""
    if len(p) == 4:
        p[0] = AST.Declare_parameter(p[1], p[3], p=p)
    else:
        if p[1] == 'BYREF':
            p[0] = AST.Declare_parameter(p[2], p[4], True, p=p)
        elif p[1] == 'BYVAL':
            p[0] = AST.Declare_parameter(p[2], p[4], False, p=p)

def p_declare_array_parameter(p):
    """declare_parameter : ID COLON ARRAY OF ID
            | BYREF ID COLON ARRAY OF ID
            | BYVAL ID COLON ARRAY OF ID"""
    if len(p) == 6:
        p[0] = AST.Declare_arr_parameter(p[1], p[5], p=p)
    else:
        if p[1] == 'BYREF':
            p[0] = AST.Declare_arr_parameter(p[2], p[6], True, p=p)
        elif p[1] == 'BYVAL':
            p[0] = AST.Declare_arr_parameter(p[2], p[6], False, p=p)

def p_new_declare_array_parameter(p):
    """declare_parameter : ID LEFT_SQUARE RIGHT_SQUARE COLON ID
            | BYREF ID LEFT_SQUARE RIGHT_SQUARE COLON ID
            | BYVAL ID LEFT_SQUARE RIGHT_SQUARE COLON ID"""
    if len(p) == 6:
        p[0] = AST.Declare_arr_parameter(p[1], p[5], p=p)
    else:
        if p[1] == 'BYREF':
            p[0] = AST.Declare_arr_parameter(p[2], p[6], True, p=p)
        elif p[1] == 'BYVAL':
            p[0] = AST.Declare_arr_parameter(p[2], p[6], False, p=p)

def p_parameters(p):
    """parameters : parameters COMMA expression
            | expression"""
    if len(p) == 2:
        p[0] = AST.Parameters(p=p)
        p[0].add_parameter(p[1])
    else:
        p[1].add_parameter(p[3])
        p[0] = p[1]

def p_procedure_statement(p):
    """statement : PROCEDURE ID LEFT_PAREN declare_parameters RIGHT_PAREN statements ENDPROCEDURE
            | PROCEDURE NEW LEFT_PAREN declare_parameters RIGHT_PAREN statements ENDPROCEDURE
            | PROCEDURE ID LEFT_PAREN RIGHT_PAREN statements ENDPROCEDURE
            | PROCEDURE NEW LEFT_PAREN RIGHT_PAREN statements ENDPROCEDURE"""
    if len(p) == 7:
        p[0] = AST.Function(p[2], None, p[5], p=p)
    else:
        p[0] = AST.Function(p[2], p[4], p[6], p=p)

def p_public_procedure_statement(p):
    """statement : PUBLIC PROCEDURE ID LEFT_PAREN declare_parameters RIGHT_PAREN statements ENDPROCEDURE
            | PUBLIC PROCEDURE NEW LEFT_PAREN declare_parameters RIGHT_PAREN statements ENDPROCEDURE
            | PUBLIC PROCEDURE ID LEFT_PAREN RIGHT_PAREN statements ENDPROCEDURE
            | PUBLIC PROCEDURE NEW LEFT_PAREN RIGHT_PAREN statements ENDPROCEDURE"""
    if len(p) == 8:
        p[0] = AST.Function(p[3], None, p[6], p=p)
    else:
        p[0] = AST.Function(p[3], p[5], p[7], p=p)

def p_private_procedure_statement(p):
    """statement : PRIVATE PROCEDURE ID LEFT_PAREN declare_parameters RIGHT_PAREN statements ENDPROCEDURE
            | PRIVATE PROCEDURE NEW LEFT_PAREN declare_parameters RIGHT_PAREN statements ENDPROCEDURE
            | PRIVATE PROCEDURE ID LEFT_PAREN RIGHT_PAREN statements ENDPROCEDURE
            | PRIVATE PROCEDURE NEW LEFT_PAREN RIGHT_PAREN statements ENDPROCEDURE"""
    if len(p) == 8:
        p[0] = AST.Function(p[3], None, p[6], private=True, p=p)
    else:
        p[0] = AST.Function(p[3], p[5], p[7], private=True, p=p)

def p_call_procedure_statement(p):
    """statement : CALL ID LEFT_PAREN parameters RIGHT_PAREN
            | CALL ID LEFT_PAREN RIGHT_PAREN"""
    if len(p) == 5:
        p[0] = AST.Call_function(p[2], p=p)
    else:
        p[0] = AST.Call_function(p[2], p[4], p=p)

def p_function_statement(p):
    """statement : FUNCTION ID LEFT_PAREN declare_parameters RIGHT_PAREN RETURNS ID statements ENDFUNCTION
            | FUNCTION ID LEFT_PAREN declare_parameters RIGHT_PAREN RETURNS ARRAY statements ENDFUNCTION
            | FUNCTION ID LEFT_PAREN RIGHT_PAREN RETURNS ID statements ENDFUNCTION
            | FUNCTION ID LEFT_PAREN RIGHT_PAREN RETURNS ARRAY statements ENDFUNCTION"""
    if len(p) == 9:
        p[0] = AST.Function(p[2], None, p[7], p[6], p=p)
    else:
        p[0] = AST.Function(p[2], p[4], p[8], p[7], p=p)

def p_public_function_statement(p):
    """statement : PUBLIC FUNCTION ID LEFT_PAREN declare_parameters RIGHT_PAREN RETURNS ID statements ENDFUNCTION
            | PUBLIC FUNCTION ID LEFT_PAREN declare_parameters RIGHT_PAREN RETURNS ARRAY statements ENDFUNCTION
            | PUBLIC FUNCTION ID LEFT_PAREN RIGHT_PAREN RETURNS ID statements ENDFUNCTION
            | PUBLIC FUNCTION ID LEFT_PAREN RIGHT_PAREN RETURNS ARRAY statements ENDFUNCTION"""
    if len(p) == 10:
        p[0] = AST.Function(p[3], None, p[8], p[7], p=p)
    else:
        p[0] = AST.Function(p[3], p[5], p[9], p[8], p=p)

def p_private_function_statement(p):
    """statement : PRIVATE FUNCTION ID LEFT_PAREN declare_parameters RIGHT_PAREN RETURNS ID statements ENDFUNCTION
            | PRIVATE FUNCTION ID LEFT_PAREN declare_parameters RIGHT_PAREN RETURNS ARRAY statements ENDFUNCTION
            | PRIVATE FUNCTION ID LEFT_PAREN RIGHT_PAREN RETURNS ID statements ENDFUNCTION
            | PRIVATE FUNCTION ID LEFT_PAREN RIGHT_PAREN RETURNS ARRAY statements ENDFUNCTION"""
    if len(p) == 10:
        p[0] = AST.Function(p[3], None, p[8], p[7], private=True, p=p)
    else:
        p[0] = AST.Function(p[3], p[5], p[9], p[8], private=True, p=p)

def p_arr_function_statement(p):
    """statement : FUNCTION ID LEFT_PAREN declare_parameters RIGHT_PAREN RETURNS ARRAY OF ID statements ENDFUNCTION
            | FUNCTION ID LEFT_PAREN RIGHT_PAREN RETURNS ARRAY OF ID statements ENDFUNCTION"""
    if len(p) == 11:
        p[0] = AST.ArrFunction(p[2], None, p[8], p[9], p=p)
    else:
        p[0] = AST.ArrFunction(p[2], p[4], p[9], p[10], p=p)

def p_public_arr_function_statement(p):
    """statement : PUBLIC FUNCTION ID LEFT_PAREN declare_parameters RIGHT_PAREN RETURNS ARRAY OF ID statements ENDFUNCTION
            | PUBLIC FUNCTION ID LEFT_PAREN RIGHT_PAREN RETURNS ARRAY OF ID statements ENDFUNCTION"""
    if len(p) == 12:
        p[0] = AST.ArrFunction(p[3], None, p[9], p[10], p=p)
    else:
        p[0] = AST.ArrFunction(p[3], p[5], p[10], p[11], p=p)

def p_private_arr_function_statement(p):
    """statement : PRIVATE FUNCTION ID LEFT_PAREN declare_parameters RIGHT_PAREN RETURNS ARRAY OF ID statements ENDFUNCTION
            | PRIVATE FUNCTION ID LEFT_PAREN RIGHT_PAREN RETURNS ARRAY OF ID statements ENDFUNCTION"""
    if len(p) == 12:
        p[0] = AST.ArrFunction(p[3], None, p[9], p[10], private=True, p=p)
    else:
        p[0] = AST.ArrFunction(p[3], p[5], p[10], p[11], private=True, p=p)

def p_call_function_expression(p):
    """expression : ID LEFT_PAREN parameters RIGHT_PAREN
            | MOD LEFT_PAREN parameters RIGHT_PAREN
            | DIV LEFT_PAREN parameters RIGHT_PAREN
            | ID LEFT_PAREN RIGHT_PAREN"""
    if len(p) == 4:
        if p[1] in insert_functions:
            p[0] = insert_functions[p[1]](None, p=p)
        else:
            p[0] = AST.Call_function(p[1], p=p)
    else:
        if p[1] in insert_functions:
            p[0] = insert_functions[p[1]](p[3], p=p)
        else:
            p[0] = AST.Call_function(p[1], p[3], p=p)

def p_return_statement(p):
    """statement : RETURN expression"""
    p[0] = AST.Return(p[2], p=p)

def p_openfile_statement(p):
    """statement : OPENFILE expression FOR READ
            | OPENFILE expression FOR WRITE
            | OPENFILE expression FOR APPEND
            | OPENFILE expression FOR RANDOM"""
    p[0] = AST.Open_file(p[2], p[4], p=p)

def p_readfile_array_statement(p):
    """statement : READFILE expression COMMA ID LEFT_SQUARE indexes RIGHT_SQUARE"""
    p[0] = AST.Read_file_array(p[2], p[4], p[6], p=p)

def p_readfile_statement(p):
    """statement : READFILE expression COMMA ID"""
    p[0] = AST.Read_file(p[2], p[4], p=p)

def p_writefile_statement(p):
    """statement : WRITEFILE expression COMMA expression"""
    p[0] = AST.Write_file(p[2], p[4], p=p)

def p_closefile_statement(p):
    """statement : CLOSEFILE expression"""
    p[0] = AST.Close_file(p[2], p=p)

def p_seek_statement(p):
    """statement : SEEK expression COMMA expression"""
    p[0] = AST.Seek(p[2], p[4], p=p)

def p_composite_type_declare_statement(p):
    """statement : TYPE ID statements ENDTYPE"""
    p[0] = AST.Composite_type(p[2], p[3], p=p)

def p_composite_type_expression(p):
    """expression : expression DOT expression"""
    p[0] = AST.Composite_type_expression(p[1], p[3])

# def p_composite_type_statement(p):
#     """statement : expression DOT statement"""
#     p[0] = AST.Composite_type_statement(p[1], p[3])

def p_enumerate_type_statement(p):
    """statement : TYPE ID EQUAL LEFT_PAREN enumerate_items RIGHT_PAREN"""
    p[0] = AST.Enumerate_type(p[2], p[5], p=p)

def p_enumerate_items(p):
    """enumerate_items : enumerate_items COMMA ID
            | ID"""
    if len(p) == 2:
        p[0] = AST.Enumerate_items(p=p)
        p[0].add_item(p[1])
    else:
        p[1].add_item(p[3])
        p[0] = p[1]

def p_pointer_expression(p):
    """expression : POINTER expression"""
    p[0] = AST.Pointer(p[2], p=p)

def p_solve_pointer_expression(p):
    """expression : expression POINTER"""
    p[0] = AST.SolvePointer(p[1], p=p)

def p_pointer_type_statement(p):
    """statement : TYPE ID EQUAL POINTER ID"""
    p[0] = AST.TypePointerStatement(p[2], p[5], p=p)

# def p_pointer_statement(p):
#     """statement : ID ASSIGN POINTER ID"""
#     p[0] = AST.PointerStatement(p[1], p[4], p=p)

def p_pass_statement(p):
    """statement : PASS"""
    p[0] = AST.Pass(p=p)

def p_import_statement(p):
    """statement : IMPORT expression"""
    p[0] = AST.Import(p[2], p=p)

def p_class_statement(p):
    """statement : CLASS ID statements ENDCLASS"""
    p[0] = AST.Class(p[2], p[3], p=p)

def p_class_inherit_statement(p):
    """statement : CLASS ID INHERITS ID statements ENDCLASS"""
    p[0] = AST.Class(p[2], p[5], p[4], p=p)

def p_class_expression(p):
    """expression : NEW ID
            | NEW ID LEFT_PAREN parameters RIGHT_PAREN"""
    if len(p) == 3:
        p[0] = AST.Class_expression(p[2], None, p=p)
    else:
        p[0] = AST.Class_expression(p[2], p[4], p=p)

def p_set_statement(p):
    """statement : TYPE ID EQUAL SET OF ID"""
