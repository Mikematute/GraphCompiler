

# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------

reserved = {
    'program' : 'PROGRAM',
    'var': 'VAR',
    'void': 'VOID',
    'main': 'MAIN',
    'int': 'INT',
    'float': 'FLOAT',
    'string': 'STRING',
    'char': 'CHAR',
    'bool': 'BOOL',
    'node': 'NODE',
    'arc': 'ARC',
    'undirected': 'UNDIRECTED',
    'directed': 'DIRECTED',
    'print': 'PRINT',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'do': 'DO',
    'deg': 'DEG',
    'shortpath': 'SHORTPATH',
    'diameter': 'DIAMETER',
    'add': 'ADD',
    'delete': 'DELETE'
}

tokens = [
    'ID', 'SCOLO', 'COMA', 'LPAREN', 
    'RPAREN', 'LCORCH', 'RCORCH', 'CTE_INT',
    'EQL',  'LBRACK', 'RBRACK', 'CTE_STRING',
    'SUMA', 'SUB', 'MUL', 'DIV', 'RESD',
    'AND', 'OR', 'MORET', 'LESST', 'MOREEQUAL',
    'LESSEQUAL', 'EQUALTO', 'NOTEQUALTO', 'NOT', 'CTE_FLO',
    'CTE_BOO', 'CTE_CHAR','DOT', 'COLON'
    ] + list(reserved.values())

# Tokens
# t_ADD    = r'\+'
# t_SUB   = r'-'
# t_TIMES   = r'\*'
# t_DIVIDE  = r'/'
# t_EQL  = r'='
# t_LPAREN  = r'\('
# t_RPAREN  = r'\)'
# t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

t_SCOLO = r';'
t_COMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCORCH = r'\['
t_RCORCH = r'\]'
t_EQL = r'='
t_LBRACK = r'{'
t_RBRACK = r'}'
t_SUMA = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'\/'
t_RESD = r'%'
t_AND = r'&&'
t_OR = r'\|\|'
t_MORET = r'>'
t_LESST = r'<'
t_MOREEQUAL = r'>='
t_LESSEQUAL = r'<='
t_EQUALTO = r'=='
t_NOTEQUALTO = r'!='
t_NOT = r'!'
t_DOT = r'\.'
t_COLON = r':'
t_CTE_STRING = r'\".*\"'
t_CTE_FLO = r'[0-9]+\.[0-9]+'
t_CTE_BOO = r'true|false'
t_CTE_CHAR = r'\'.\''


def t_ID(t):
    r'[a-z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_CTE_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Parsing rules
'''
precedence = (
    ('left','ADD','SUB'),
    ('left','TIMES','DIVIDE'),
    ('right','USUB'),
    )
'''
import ply.yacc as yacc

# from calclex import tokens

def p_program(t):
    'program : ID SCOLO vars function body'
    # print("enters program")

def p_vars(t):
    '''vars : VAR type vars_1 SCOLO vars
                | empty'''
    # if t[1] == 'VAR':
       #  print("enter var")
    # else:
       #  print("enter empty")

def p_vars_1(t):
    '''vars_1 : ID
              | ID COMA ID'''
    # if t[2] == 'COMA':
        # print("enter ID COMA ID")
    # else:
        # print("enter ID")

def p_function(t):
    '''function : function_t ID LPAREN function_v RPAREN LBRACK vars statutes RBRACK
                | empty'''
    # print("enters function")

def p_function_t(t):
    '''function_t : VOID
                    | t_number
                    | t_string
                    | t_bool
                    | t_graph'''

def p_function_v(t):
    '''function_v : function_v1
                    | empty'''

def p_function_v1(t):
    '''function_v1 : type ID COMA
                    | type ID COMA function_v1'''

def p_body(t):
    'body : MAIN LPAREN RPAREN LBRACK vars statutes RBRACK'

def p_type(t):
    '''type : t_number
            | t_string
            | t_bool
            | t_graph
            | t_array'''

def p_t_number(t):
    '''t_number : INT
                | FLOAT'''

def p_t_string(t):
    '''t_string : STRING
                | CHAR'''

def p_t_bool(t):
    't_bool : BOOL'

def p_t_graph(t):
    '''t_graph : NODE
                | ARC
                | UNDIRECTED
                | DIRECTED'''

def p_t_array(t):
    't_array : t_array_1 LCORCH CTE_INT RCORCH t_array_2'

def p_t_array_1(t):
    '''t_array_1 : t_number
                | t_string
                | t_bool
                | t_graph'''

def p_t_array_2(t):
    '''t_array_2 : LCORCH CTE_INT RCORCH t_array_2
                | empty'''

def p_t_statutes(t):
    '''statutes : statutes_1 statutes
                | empty'''

def p_t_statutes_1(t):
    '''statutes_1 : assignation
                    | writting
                    | condition
                    | cycle'''

def p_assignation(t):
    'assignation : ID EQL expression'



def p_empty(p):
    'empty :'
    pass

def p_error(t):
    print("Syntax error at '%s'" % t.value)

parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')   # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s)



