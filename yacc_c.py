################################################################################
#                         G L O B A L  H A N D L E R S                         #
################################################################################

from tables import Tables
globalVars = Tables();

################################################################################
#                                 T O K E N S                                  #
################################################################################

reserved = {
    'program'   : 'PROGRAM',
    'var'       : 'VAR',
    'void'      : 'VOID',
    'main'      : 'MAIN',
    'int'       : 'INT',
    'float'     : 'FLOAT',
    'string'    : 'STRING',
    'char'      : 'CHAR',
    'bool'      : 'BOOL',
    'node'      : 'NODE',
    'arc'       : 'ARC',
    'undirected': 'UNDIRECTED',
    'directed'  : 'DIRECTED',
    'print'     : 'PRINT',
    'if'        : 'IF',
    'else'      : 'ELSE',
    'while'     : 'WHILE',
    'do'        : 'DO',
    'for'       : 'FOR',
    'in'        : 'IN',
    'deg'       : 'DEG',
    'shortpath' : 'SHORTPATH',
    'diameter'  : 'DIAMETER',
    'add'       : 'ADD',
    'delete'    : 'DELETE'
}

tokens = [
    'ID',       'SCOLO',        'COMA',         'LPAREN',   'RPAREN',
    'LCORCH',   'RCORCH',       'CTE_INT',      'EQL',      'LBRACK',
    'RBRACK',   'CTE_STRING',   'SUMA',         'SUB',      'MUL',
    'DIV',      'RESD',         'AND',          'OR',       'MORET',
    'LESST',    'MOREEQUAL',    'LESSEQUAL',    'EQUALTO',  'NOTEQUALTO',
    'NOT',      'CTE_FLO',      'CTE_BOO',      'CTE_CHAR', 'DOT',
    'COLON'
    ] + list(reserved.values())

t_SCOLO =       r';'
t_COMA =        r','
t_LPAREN =      r'\('
t_RPAREN =      r'\)'
t_LCORCH =      r'\['
t_RCORCH =      r'\]'
t_EQL =         r'='
t_LBRACK =      r'{'
t_RBRACK =      r'}'
t_SUMA =        r'\+'
t_SUB =         r'-'
t_MUL =         r'\*'
t_DIV =         r'\/'
t_RESD =        r'%'
t_AND =         r'&&'
t_OR =          r'\|\|'
t_MORET =       r'>'
t_LESST =       r'<'
t_MOREEQUAL =   r'>='
t_LESSEQUAL =   r'<='
t_EQUALTO =     r'=='
t_NOTEQUALTO =  r'!='
t_NOT =         r'!'
t_DOT =         r'\.'
t_COLON =       r':'
t_CTE_STRING =  r'\"[^"]*\"'
t_CTE_FLO =     r'[0-9]+\.[0-9]+'
t_CTE_BOO =     r'true|false'
t_CTE_CHAR =    r'\'.\''

def t_ID(t):
    r'[a-z][a-z|A-Z|0-9]*'
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
################################################################################
#                                  R U L E S                                   #
################################################################################
# Parsing rules
'''
precedence = (
    ('left','ADD','SUB'),
    ('left','TIMES','DIVIDE'),
    ('right','USUB'),
    )
'''
import ply.yacc as yacc
import time

################################ P R O G R A M ################################
def p_program(t):
    'program : PROGRAM ID np_var_a1 SCOLO np_var_a2 vars function body'
################################### V A R S ####################################
def p_vars(t):
    '''vars : VAR type vars_1 SCOLO vars
            | empty'''

def p_vars_1(t):
    '''vars_1 : ID np_var_2 vars_2
              | ID np_var_2 vars_2 COMA vars_1'''

def p_vars_2(t):
    '''vars_2 : array_declare
              | empty'''

############################### F U N C T I O N ################################
def p_function(t):
    '''function : function_t ID np_var_b2 np_var_b3 LPAREN function_v RPAREN LBRACK vars statutes RBRACK function
                | empty'''

def p_function_t(t):
    '''function_t : VOID np_var_1
                  | t_number
                  | t_string
                  | t_bool
                  | t_graph'''

def p_function_v(t):
    '''function_v : function_v1
                  | empty'''

def p_function_v1(t):
    '''function_v1 : type np_var_b4 ID np_var_b5
                   | type np_var_b4 ID np_var_b5 COMA function_v1
                   | type np_var_b4 ID np_var_b5 array_declare
                   | type np_var_b4 ID np_var_b5 array_declare COMA function_v1'''
#################################### B O D Y ###################################
def p_body(t):
    'body : MAIN np_var_c1 LPAREN RPAREN LBRACK np_var_c2 vars statutes RBRACK debug np_var_c3'
#################################### T Y P E ###################################
def p_type(t):
    '''type : t_number
            | t_string
            | t_bool
            | t_graph'''

def p_t_number(t):
    '''t_number : INT np_var_1
                | FLOAT np_var_1'''

def p_t_string(t):
    '''t_string : STRING np_var_1
                | CHAR np_var_1'''

def p_t_bool(t):
    't_bool : BOOL np_var_1'

def p_t_graph(t):
    '''t_graph : NODE np_var_1
               | ARC np_var_1
               | UNDIRECTED np_var_1
               | DIRECTED np_var_1'''
########################### A R R A Y _ D E C L A R E ##########################
def p_array_declare(t):
    'array_declare : LCORCH CTE_INT RCORCH array_declare_1'

def p_array_declare_1(t):
    '''array_declare_1 : LCORCH CTE_INT RCORCH array_declare_1
                       | empty'''
################################ S T A T U T E S ###############################
def p_statutes(t):
    '''statutes : statutes_1 statutes
                | empty'''

def p_statutes_1(t):
    '''statutes_1 : assignation
                  | writing
                  | condition
                  | cycle
                  | function_call'''
#---------------------------- a s s i g n a t i o n ----------------------------
def p_assignation(t):
    'assignation : ID EQL expression SCOLO'
#------------------------------- w r i t i n g ---------------------------------
def p_writing(t):
    'writing : PRINT LPAREN writing_1 RPAREN SCOLO'

def p_writing_1(t):
    '''writing_1 : expression
                 | CTE_STRING
                 | writing_2'''


def p_writing_2(t):
    '''writing_2 : expression SUMA writing_1
                 | CTE_STRING SUMA writing_1'''
#------------------------------ c o n d i t i o n ------------------------------
def p_condition(t):
    'condition : IF LPAREN expression RPAREN LBRACK statutes RBRACK condition_1'

def p_condition_1(t):
    '''condition_1 : ELSE LBRACK statutes RBRACK
                   | empty'''
#--------------------------------- c y c l e -----------------------------------
def p_cycle(t):
    '''cycle : c_while
             | c_do
             | c_for
             | c_forin'''

def p_c_while(t):
    'c_while : WHILE LPAREN expression RPAREN LBRACK statutes RBRACK'

def p_c_do(t):
    'c_do : DO LBRACK statutes RBRACK WHILE LPAREN expression RPAREN SCOLO'

def p_c_for(t):
    'c_for : FOR LPAREN ID SCOLO expression SCOLO assignation RPAREN LBRACK statutes RBRACK'

def p_c_forin(t):
    'c_forin : FOR LPAREN ID IN ID RPAREN LBRACK statutes RBRACK'
#------------------------- f u n c t i o n _ c a l l ---------------------------
def p_function_call(t):
    'function_call : ID LPAREN function_call_1 RPAREN SCOLO'

def p_function_call_1(t):
    '''function_call_1 : function_call_2
                       | empty'''

def p_function_call_2(t):
    '''function_call_2 : expression
                       | ID
                       | expression SCOLO function_call_2
                       | ID SCOLO function_call_2'''

############################## E X P R E S S I O N #############################
def p_expression(t):
    '''expression : exp_lv1
                  | exp_lv1 AND expression
                  | exp_lv1 OR expression'''

def p_exp_lv1(t):
    'exp_lv1 : exp_lv2 exp_lv1_1'
def p_exp_lv1_1(t):
    '''exp_lv1_1 : LESST exp_lv2
                 | MORET exp_lv2
                 | LESSEQUAL exp_lv2
                 | MOREEQUAL exp_lv2
                 | EQUALTO exp_lv2
                 | NOTEQUALTO exp_lv2
                 | empty'''

def p_exp_lv2(t):
    '''exp_lv2 : exp_lv3
               | exp_lv3 SUMA exp_lv2
               | exp_lv3 SUB exp_lv2'''

def p_exp_lv3(t):
    '''exp_lv3 : exp_lv4
               | exp_lv4 MUL exp_lv3
               | exp_lv4 DIV exp_lv3
               | exp_lv4 RESD exp_lv3'''

def p_exp_lv4(t):
    '''exp_lv4 : exp_lv5
               | NOT exp_lv5'''

def p_exp_lv5(t):
    '''exp_lv5 : RPAREN expression LPAREN
               | var_cte
               | method
               | ID
               | ID array_access'''

############################ A R R A Y _ A C C E S S ###########################
def p_array_access(t):
    'array_access : LCORCH arrary_access_1 RCORCH arrary_access_2'

def p_array_access_1(t):
    '''arrary_access_1 : CTE_INT
                       | ID'''

def p_array_access_2(t):
    '''arrary_access_2 : LCORCH arrary_access_1 RCORCH arrary_access_2
                       | empty'''
################################# V A R _ C T E ################################
def p_var_cte(t):
    '''var_cte : CTE_INT
               | CTE_FLO
               | CTE_BOO
               | CTE_STRING
               | CTE_CHAR'''
    print("var_cte")
    print(t[1])

################################## M E T H O D #################################
def p_method(t):
    'method : ID DOT method_t LPAREN method_1 RPAREN'

def p_method_1(t):
    '''method_1 : method_1_1
                | empty'''

def p_method_1_1(t):
    '''method_1_1 : method_v
                  | method_v COMA method_1_1'''

def p_method_t(t):
    '''method_t : DEG
                | SHORTPATH
                | DIAMETER
                | ADD
                | DELETE
                | ARC'''

def p_method_v(t):
    '''method_v : ID
                | LBRACK ID COMA ID RBRACK'''

################################################################################
#                        N E U R A L T I C   P O I N T S                       #
################################################################################

######################## A D D I N G  V A R I A B L E S ########################

#-------------------------------- g l o b a l ----------------------------------
def p_np_var_a1(t):
    'np_var_a1 : empty'
    # Save the name of the global context (program ID)
    globalVars.globalContext = t[-1];
    # Stablish the current context to global
    globalVars.currentContext = globalVars.globalContext;
    # Add the ID to the directions table with its details
    globalVars.auxType = "void";
    globalVars.add_dir();

def p_np_var_a2(t):
    'np_var_a2 : empty'
    # Create the table of global variables
    globalVars.dicDirections[globalVars.globalContext]['vars'] = {};

#----------------------------- f u n c t i o n s -------------------------------
def p_np_var_b1(t):
    'np_var_b1 : empty'
    # Store the function type
    globalVars.auxType = t[-1];

def p_np_var_b2(t):
    'np_var_b2 : empty'
    # Store the function ID
    globalVars.auxID = t[-1];
    # Add the function ID and function TYPE to the directions table as long as it
    # doesn't exist
    if globalVars.auxID not in globalVars.dicDirections:
        # Stablish the current context to the function ID
        globalVars.currentContext = globalVars.auxID;
        globalVars.add_dir();

    else:
        print ('ERROR: Function: <{0}>, already declared'.format(globalVars.auxID));

def p_np_var_b3(t):
    'np_var_b3 : empty'
    # Create the table of function variables
    globalVars.dicDirections[globalVars.currentContext]['vars'] = {};

def p_np_var_b4(t):
    'np_var_b4 : empty'
    # Saves the variable type
    globalVars.auxType = t[-1];

def p_np_var_b5(t):
    'np_var_b5 : empty'
    # Saves the variable ID
    globalVars.auxID = t[-1];
    # If the variable ID doesn't exists in the current context variable table,
    # nor in the global variable table...
    if not globalVars.exists_in_global():
        if not globalVars.exists_in_local():
            # ... then adds a new entry
            globalVars.add_var();
        else:
            print ('ERROR: Variable: <{0}>, in function: <{1}> already declared'.format(globalVars.auxID, globalVars.currentContext));
    else:
        print ('ERROR: Variable: <{0}>, in function: <{1}> already declared as global'.format(globalVars.auxID, globalVars.currentContext));

#---------------------------------- m a i n ------------------------------------
def p_np_var_c1(t):
    'np_var_c1 : empty'
    # sets the current context to MAIN
    globalVars.currentContext = "main";
    # sets the current type of MAIN to VOID
    globalVars.auxType = "void";
    # adds MAIN to the direction table
    globalVars.add_dir();

def p_np_var_c2(t):
    'np_var_c2 : empty'
    # Creates the table of main variables
    globalVars.dicDirections['main']['vars'] = {};

def p_np_var_c3(t):
    'np_var_c3 : empty'
    # Erases the table of direction and variables generated
    globalVars.reset_tables();
    print ("ERASING ALL TABLES\n");
    time.sleep(1.5);

#------------------------------ v a r s  r u l e -------------------------------
def p_np_var_1(t):
    'np_var_1 : empty'
    # Store the type of the variable
    globalVars.auxType = t[-1];

def p_np_var_2(t):
    'np_var_2 : empty'
    # Store the ID of the variable
    globalVars.auxID = t[-1];
    # If the variable ID doesn't exists in the current context variable table,
    # nor in the global variable table...
    if not globalVars.exists_in_global():
        if not globalVars.exists_in_local():
            # ... then adds a new entry
            globalVars.add_var();
        else:
            print ('ERROR: Variable: <{0}>, in function: <{1}> already declared'.format(globalVars.auxID, globalVars.currentContext));
    else:
        print ('ERROR: Variable: <{0}>, in function: <{1}> already declared as global'.format(globalVars.auxID, globalVars.currentContext));
################################## O T H E R S #################################
def p_debug(t):
    'debug : empty'
    print("\n" + "DEBUGGING TABLES" + "\n");
    time.sleep(1.5);
    globalVars.print_tables();
    print("\n" + "END OF DEBBUGGER" + "\n");

def p_empty(p):
    'empty :'
    pass

def p_error(t):
    print("Syntax error at '%s'" % t.value)

################################################################################
#                            M A I N  P R O G R A M                            #
################################################################################
parser = yacc.yacc()

while True:
    try:
        s = input('WOOF > ')   # Use raw_input on Python 2
        print ("\n");
    except EOFError:
        break
    parser.parse(s)
