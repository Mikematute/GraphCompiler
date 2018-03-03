

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
t_CTE_BOO = r'True|False'
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

# dictionary of names
names = { }

def p_statement_assign(t):
    'statement : NAME EQL expression'
    names[t[1]] = t[3]

def p_statement_expr(t):
    'statement : expression'
    print(t[1])

def p_expression_binop(t):
    expression : expression ADD expression
                  | expression SUB expression
                  | expression TIMES expression
                  | expression DIVIDE expression
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

def p_expression_uSUB(t):
    'expression : SUB expression %prec USUB'
    t[0] = -t[2]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]

def p_expression_name(t):
    'expression : NAME'
    try:
        t[0] = names[t[1]]
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')   # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s)
'''


