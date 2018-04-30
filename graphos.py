################################################################################
#                         G L O B A L  H A N D L E R S                         #
################################################################################

from table import Table
from oracle import consult
from memory import Memory
from algorithmQuadruple import Algorithm_Quadruple
from virtualMachine import Virtual_Machine
import sys


global_mem   = Memory(1)
local_mem    = Memory(2)
temporal_mem = Memory(3)
constant_mem = Memory(4)
globalVars   = Table()
alg_quad     = Algorithm_Quadruple()

operator_conv = { '+'   : 0,
                  '-'   : 1,
                  '*'   : 2,
                  '/'   : 3,
                  '='   : 4,
                  '%'   : 5,
                  '&&'  : 6,
                  '||'  : 7,
                  '<'   : 8,
                  '>'   : 9,
                  '<='  : 10,
                  '>='  : 11,
                  '!='  : 12,
                  '=='  : 13,
                  '!'   : 14,
                  'print': 15}

type_conv = {     'int'     : 0,
                  'float'   : 1,
                  'char'    : 2,
                  'string'  : 3,
                  'bool'    : 4,
                  'node'    : 5,
                  'arc'     : 6,
                  'directed': 7,
                  'undirected': 8}

testing_temp = 0
################################################################################
#                                 T O K E N S                                  #
################################################################################

reserved = {
    'program'   : 'PROGRAM',
    'return'    : 'RETURN',
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
    'addNode'   : 'ADDNODE',
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
t_CTE_BOO =     r'True|False'
t_CTE_CHAR =    r'\'.\''

def t_ID(t):
    r'[a-z][a-z|A-Z|0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_CTE_INT(t):
    r'-?\d+'
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
#                                                                              #
#                                  R U L E S                                   #
#                                                                              #
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
    'program : PROGRAM ID np_var_a1 SCOLO np_var_a2 vars np_goto_main function body'

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
    '''function : function_t ID np_var_b2 np_var_b3 LPAREN function_v RPAREN LBRACK vars statutes RBRACK np_var_b6 function
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
    'body : MAIN np_var_c1 LPAREN RPAREN LBRACK np_var_c2 vars statutes RBRACK np_eof debug np_var_c3'

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
    'array_declare : np_var_3 LCORCH CTE_INT np_var_4 RCORCH array_declare_1 np_var_7'

def p_array_declare_1(t):
    '''array_declare_1 : np_var_5 LCORCH CTE_INT np_var_6 RCORCH
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
                  | function_call SCOLO
                  | method
                  | return'''
#---------------------------- a s s i g n a t i o n ----------------------------
def p_assignation(t):
    '''assignation : ID np_quad_a2 EQL np_quad_b expression np_quad_assign SCOLO
                   | ID np_quad_a2 array_access EQL np_quad_b expression np_quad_assign SCOLO'''

#------------------------------- w r i t i n g ---------------------------------
def p_writing(t):
    'writing : PRINT np_quad_b LPAREN writing_1 RPAREN np_quad_print SCOLO'

def p_writing_1(t):
    'writing_1 : expression'

def p_writing_2(t):
    'writing_2 : expression SUMA np_quad_b writing_1 np_quad_c2'

#------------------------------ c o n d i t i o n ------------------------------
def p_condition(t):
    'condition : IF LPAREN expression np_statutes_a1 RPAREN LBRACK statutes RBRACK condition_1 np_statutes_a3'

def p_condition_1(t):
    '''condition_1 : ELSE np_statutes_a2 LBRACK statutes RBRACK
                   | empty'''
#--------------------------------- c y c l e -----------------------------------
def p_cycle(t):
    '''cycle : c_while
             | c_do
             | c_for
             | c_forin'''

def p_c_while(t):
    'c_while : WHILE np_statutes_b1 LPAREN expression RPAREN np_statutes_b2 LBRACK statutes RBRACK np_statutes_b3'

def p_c_do(t):
    'c_do : DO np_statutes_c1 LBRACK statutes RBRACK WHILE LPAREN expression RPAREN SCOLO np_statutes_c2'

def p_c_for(t):
    'c_for : FOR LPAREN ID SCOLO np_statutes_d1 expression np_statutes_d2 SCOLO assignation np_statutes_d3 RPAREN LBRACK statutes RBRACK np_statutes_d4'

def p_c_forin(t):
    'c_forin : FOR LPAREN ID IN ID RPAREN LBRACK statutes RBRACK'
#------------------------- f u n c t i o n _ c a l l ---------------------------
def p_function_call(t):
    '''function_call : ID LPAREN np_era function_call_1 RPAREN np_gosub
                      | ID LPAREN np_era RPAREN np_gosub'''

def p_function_call_1(t):
    '''function_call_1 : expression np_param
                       | expression np_param COMA function_call_1
                       '''

#-------------------------------- r e t u r n ----------------------------------
def p_return(t):
    'return : RETURN expression np_return SCOLO'

############################## E X P R E S S I O N #############################
def p_expression(t):
    '''expression : exp_lv1
                  | exp_lv1 AND np_quad_b expression np_quad_c0
                  | exp_lv1 OR np_quad_b expression np_quad_c0'''

def p_exp_lv1(t):
    'exp_lv1 : exp_lv2 exp_lv1_1'
def p_exp_lv1_1(t):
    '''exp_lv1_1 : LESST np_quad_b exp_lv2 np_quad_c1
                 | MORET np_quad_b exp_lv2 np_quad_c1
                 | LESSEQUAL np_quad_b exp_lv2 np_quad_c1
                 | MOREEQUAL np_quad_b exp_lv2 np_quad_c1
                 | EQUALTO np_quad_b exp_lv2 np_quad_c1
                 | NOTEQUALTO np_quad_b exp_lv2 np_quad_c1
                 | empty'''

def p_exp_lv2(t):
    '''exp_lv2 : exp_lv3
               | exp_lv3 SUMA np_quad_b exp_lv2 np_quad_c2
               | exp_lv3 SUB np_quad_b exp_lv2 np_quad_c2'''

def p_exp_lv3(t):
    '''exp_lv3 : exp_lv4
               | exp_lv4 MUL np_quad_b exp_lv3 np_quad_c3
               | exp_lv4 DIV np_quad_b exp_lv3 np_quad_c3
               | exp_lv4 RESD np_quad_b exp_lv3 np_quad_c3'''

def p_exp_lv4(t):
    '''exp_lv4 : exp_lv5
               | NOT np_quad_b exp_lv5 np_quad_c4'''

def p_exp_lv5(t):
    '''exp_lv5 : RPAREN expression LPAREN
               | var_cte
               | function_call
               | ID np_quad_a2
               | ID np_quad_a2 array_access'''

############################ A R R A Y _ A C C E S S ###########################
def p_array_access(t):
    'array_access : np_quad_d1 LCORCH arrary_access_1 np_quad_d2 RCORCH arrary_access_2 np_quad_d5'

def p_array_access_1(t):
    '''arrary_access_1 : CTE_INT np_quad_a1_int
                       | ID np_quad_a2'''

def p_array_access_2(t):
    '''arrary_access_2 : np_quad_d3 LCORCH arrary_access_1 np_quad_d4 RCORCH
                       | empty'''
################################# V A R _ C T E ################################
def p_var_cte(t):
    '''var_cte : CTE_INT np_quad_a1_int
               | CTE_FLO np_quad_a1_flt
               | CTE_BOO np_quad_a1_bol
               | CTE_STRING np_quad_a1_str
               | CTE_CHAR np_quad_a1_chr'''

################################## M E T H O D #################################
def p_method(t):

    'method : ID CTE_INT DOT method_t'

def p_method_t(t):
    '''method_t : DEG
                | SHORTPATH
                | DIAMETER
                | ADDNODE LPAREN expression RPAREN
                | DELETE
                | ARC'''


################################################################################
#                                                                              #
#                        N E U R A L T I C   P O I N T S                       #
#                                                                              #
################################################################################

######################## A D D I N G  V A R I A B L E S ########################

#-------------------------------- g l o b a l ----------------------------------
def p_np_var_a1(t):
    'np_var_a1 : empty'
    # Save the name of the global context (program ID)
    globalVars.global_context = t[-1]
    # Stablish the current context to global
    globalVars.current_context = globalVars.global_context
    # Add the ID to the directions table with its details
    globalVars.aux_type = "void"
    globalVars.add_dir()

def p_np_var_a2(t):
    'np_var_a2 : empty'
    # Create the table of global variables
    #globalVars.table_functions[globalVars.global_context]

#----------------------------- f u n c t i o n s -------------------------------
def p_np_var_b1(t):
    'np_var_b1 : empty'
    # Store the function type
    globalVars.aux_type = t[-1];

def p_np_var_b2(t):
    'np_var_b2 : empty'
    # Store the function ID
    globalVars.aux_ID = t[-1];
    # Add the function ID and function TYPE to the directions table as long as it
    # doesn't exist
    if globalVars.aux_ID not in globalVars.table_functions:
        # Stablish the current context to the function ID
        globalVars.current_context = globalVars.aux_ID;
        globalVars.add_dir();

    else:
        print ('ERROR: Function: <{0}>, already declared'.format(globalVars.aux_ID));

def p_np_var_b3(t):
    'np_var_b3 : empty'
    # Create the table of function variables
    globalVars.table_functions[globalVars.current_context]
    # Saves the quadruple where the function begins
    function_name = globalVars.current_context
    globalVars.table_functions[function_name].init_quadruple = alg_quad.instruction_pointer + 1
    # If the type is different from void then save it as a global variable
    if globalVars.aux_type != "void":
      # Get a memory value from the global memory
      global_mem.save_memory_value("", globalVars.aux_type)
      temp_memID = global_mem.get_counter(globalVars.aux_type)
      # Get the function name
      function_name = globalVars.global_context
      # Get the current context
      aux_current = globalVars.current_context
      # Change the current context to global context
      globalVars.current_context = globalVars.global_context
      # Save the variable
      globalVars.add_var(temp_memID);
      # Restablish the current context
      globalVars.current_context = aux_current

def p_np_var_b4(t):
    'np_var_b4 : empty'
    # Saves the variable type
    #globalVars.aux_type = t[-1];

def p_np_var_b5(t):
    'np_var_b5 : empty'
    # Saves the variable ID
    globalVars.aux_ID = t[-1];
    # If the variable ID doesn't exists in the current context variable table,
    # nor in the global variable table...
    if not globalVars.exists_in_global():
        if not globalVars.exists_in_local():
            if globalVars.current_context == globalVars.global_context:
                # ... then ask for a "memory id" from the "global memory"
                global_mem.save_memory_value("", globalVars.aux_type)
                temp_memID = global_mem.get_counter(globalVars.aux_type)
            else:
                # ... then ask for a "memory id" from the "local memory"
                local_mem.save_memory_value("", globalVars.aux_type)
                temp_memID = local_mem.get_counter(globalVars.aux_type)

            # Adds a new entry to the table
            globalVars.add_var(temp_memID);
            # Adds the variable type to the parameters table
            globalVars.table_functions[globalVars.current_context].add_parameter(globalVars.aux_type)
        else:
            print ('ERROR: Variable: <{0}>, in function: <{1}> already declared'.format(globalVars.aux_ID, globalVars.current_context));
            p_error(t)
    else:
        print ('ERROR: Variable: <{0}>, in function: <{1}> already declared as global'.format(globalVars.aux_ID, globalVars.current_context));
        p_error(t)

def p_np_var_b6(t):
    'np_var_b6 : empty'
    # Erease the current vars-table
    #globalVars.delete_dir(globalVars.current_context)
    # Reset the "memory ID counter" from the "local memory"
    local_mem.reset_cont()
    # Reseting the "memory ID counter" from "temporal memory"
    temporal_mem.reset_cont()
    # We also need to add the end of the function quadruple.
    alg_quad.add_quadruple('ENDPROC', '', '', '')

#---------------------------------- m a i n ------------------------------------
def p_np_var_c1(t):
    'np_var_c1 : empty'
    # Fill the pending jump so the program can start from main
    aux_jump = alg_quad.pop_jump()
    alg_quad.instruction_pointer = alg_quad.instruction_pointer + 1
    alg_quad.fill_jump(aux_jump)
    alg_quad.instruction_pointer = alg_quad.instruction_pointer - 1
    # sets the current context to MAIN
    globalVars.current_context = "main";
    # sets the current type of MAIN to VOID
    globalVars.aux_type = "void";
    # adds MAIN to the direction table
    globalVars.add_dir();

def p_np_var_c2(t):
    'np_var_c2 : empty'
    # Creates the table of main variables
    globalVars.table_functions['main']
    # Saves the quadruple where the main begins
    globalVars.table_functions['main'].init_quadruple = alg_quad.instruction_pointer + 1

def p_np_var_c3(t):
    'np_var_c3 : empty'
    # Erases the table of direction and variables generated
    #globalVars.reset_tables();
    #print ("ERASING ALL TABLES\n");
    time.sleep(1.5);

#------------------------------ v a r s  r u l e -------------------------------
def p_np_var_1(t):
    'np_var_1 : empty'
    # Store the type of the variable
    globalVars.aux_type = t[-1];

def p_np_var_2(t):
    'np_var_2 : empty'
    # Store the ID of the variable
    globalVars.aux_ID = t[-1];
    # If the variable ID doesn't exists in the current context variable table,
    # nor in the global variable table...
    if not globalVars.exists_in_global():
        if not globalVars.exists_in_local():
            if globalVars.current_context == globalVars.global_context:
                # ... then ask for a "memory id" from the "global memory"
                global_mem.save_memory_value("", globalVars.aux_type)
                temp_memID = global_mem.get_counter(globalVars.aux_type)
            else:
                # ... then ask for a "memory id" from the "local memory"
                local_mem.save_memory_value("", globalVars.aux_type)
                temp_memID = local_mem.get_counter(globalVars.aux_type)

            # Adds a new entry to the table
            globalVars.add_var(temp_memID);
        else:
            print ('ERROR: Variable: <{0}>, in function: <{1}> already declared'.format(globalVars.aux_ID, globalVars.current_context));
            p_error(t)
    else:
        print ('ERROR: Variable: <{0}>, in function: <{1}> already declared as global'.format(globalVars.aux_ID, globalVars.current_context));
        p_error(t)

def p_np_var_3(t):
    'np_var_3 : empty'
    # Since we now know it is a dimentional variable, we open up the dimensional variable and assin its starting dimensions
    id_var = globalVars.aux_ID
    globalVars.reset_dim()

    if globalVars.variable_in_global(id_var) :
        # We initialize the table that will save all the proper attributes to calculate dimesions
        globalVars.table_functions[globalVars.global_context].vars_table[id_var].dimension['inf'] = 0
        globalVars.table_functions[globalVars.global_context].vars_table[id_var].dimension['sup'] = 0
        globalVars.table_functions[globalVars.global_context].vars_table[id_var].dimension['aux'] = 0
        globalVars.table_functions[globalVars.global_context].vars_table[id_var].dimension['next'] = {}


    # If it doesn't exist as global. Check if the "id" exists in the local variable table
    elif globalVars.variable_in_local(id_var) :
        # We initialize the table that will save all the proper attributes to calculate dimesions
        globalVars.table_functions[globalVars.current_context].vars_table[id_var].dimension['inf'] = 0
        globalVars.table_functions[globalVars.current_context].vars_table[id_var].dimension['sup'] = 0
        globalVars.table_functions[globalVars.current_context].vars_table[id_var].dimension['aux'] = 0
        globalVars.table_functions[globalVars.current_context].vars_table[id_var].dimension['next'] = {}

    # The variable specified was not declared
    else:
        print ('ERROR: Variable: <{0}>, in function: <{1}> was not declared'.format(id_var, globalVars.current_context));
        p_error(t)

def p_np_var_4(t):
    'np_var_4 : empty'
    # Since we now know it is a dimentional variable, we open up the dimensional variable and assin its starting dimensions
    id_var = globalVars.aux_ID
    lim_sup = t[-1];

    if globalVars.variable_in_global(id_var) :
        # We initialize the table that will save all the proper attributes to calculate dimesions
        curr_cont = globalVars.global_context

    # If it doesn't exist as global. Check if the "id" exists in the local variable table
    elif globalVars.variable_in_local(id_var) :
        # We initialize the table that will save all the proper attributes to calculate dimesions
        curr_cont = globalVars.current_context

    # The variable specified was not declared
    else:
        print ('ERROR: Variable: <{0}>, in function: <{1}> was not declared'.format(id_var, globalVars.current_context));
        p_error(t)

    globalVars.table_functions[curr_cont].vars_table[id_var].dimension['sup'] = lim_sup
    globalVars.R = (lim_sup - 0 + 1) * globalVars.R

def p_np_var_5(t):
    'np_var_5 : empty'
    # Since we now know it is a dimentional variable, we open up the dimensional variable and assin its starting dimensions
    id_var = globalVars.aux_ID

    if globalVars.variable_in_global(id_var) :
        # We initialize the table that will save all the proper attributes to calculate dimesions
        globalVars.table_functions[globalVars.global_context].vars_table[id_var].dimension['next']['inf'] = 0
        globalVars.table_functions[globalVars.global_context].vars_table[id_var].dimension['next']['sup'] = 0
        globalVars.table_functions[globalVars.global_context].vars_table[id_var].dimension['next']['aux'] = 0



    # If it doesn't exist as global. Check if the "id" exists in the local variable table
    elif globalVars.variable_in_local(id_var) :
        # We initialize the table that will save all the proper attributes to calculate dimesions
        globalVars.table_functions[globalVars.current_context].vars_table[id_var].dimension['next']['inf'] = 0
        globalVars.table_functions[globalVars.current_context].vars_table[id_var].dimension['next']['sup'] = 0
        globalVars.table_functions[globalVars.current_context].vars_table[id_var].dimension['next']['aux'] = 0

    # The variable specified was not declared
    else:
        print ('ERROR: Variable: <{0}>, in function: <{1}> was not declared'.format(id_var, globalVars.current_context));
        p_error(t)

def p_np_var_6(t):
    'np_var_6 : empty'
    # Since we now know it is a dimentional variable, we open up the dimensional variable and assin its starting dimensions
    id_var = globalVars.aux_ID
    lim_sup = t[-1];

    if globalVars.variable_in_global(id_var) :
        # We initialize the table that will save all the proper attributes to calculate dimesions
        curr_cont = globalVars.global_context

    # If it doesn't exist as global. Check if the "id" exists in the local variable table
    elif globalVars.variable_in_local(id_var) :
        # We initialize the table that will save all the proper attributes to calculate dimesions
        curr_cont = globalVars.current_context

    # The variable specified was not declared
    else:
        print ('ERROR: Variable: <{0}>, in function: <{1}> was not declared'.format(id_var, globalVars.current_context));
        p_error(t)

    globalVars.table_functions[curr_cont].vars_table[id_var].dimension['next']['sup'] = lim_sup
    globalVars.R = (lim_sup - 0 + 1) * globalVars.R

def p_np_var_7(t):
    'np_var_7 : empty'
    # Since we now know it is a dimentional variable, we open up the dimensional variable and assin its starting dimensions
    id_var = globalVars.aux_ID

    if globalVars.variable_in_global(id_var) :
        # We initialize the table that will save all the proper attributes to calculate dimesions
        curr_cont = globalVars.global_context

    # If it doesn't exist as global. Check if the "id" exists in the local variable table
    elif globalVars.variable_in_local(id_var) :
        # We initialize the table that will save all the proper attributes to calculate dimesions
        curr_cont = globalVars.current_context

    # The variable specified was not declared
    else:
        print ('ERROR: Variable: <{0}>, in function: <{1}> was not declared'.format(id_var, globalVars.current_context));
        p_error(t)

    if globalVars.table_functions[globalVars.current_context].vars_table[id_var].dimension['next']:
      globalVars.table_functions[globalVars.current_context].vars_table[id_var].dimension['aux'] = globalVars.R / (globalVars.table_functions[curr_cont].vars_table[id_var].dimension['sup'] - 0 + 1)

    if globalVars.current_context == globalVars.global_context:
        # ... then ask for a "memory id" from the "global memory"
        for i in range(globalVars.R - 1):
          global_mem.save_memory_value("", globalVars.aux_type)
          temp_memID = global_mem.get_counter(globalVars.aux_type)
    else:
        # ... then ask for a "memory id" from the "local memory"
        for i in range(globalVars.R - 1):
          local_mem.save_memory_value("", globalVars.aux_type)
          temp_memID = local_mem.get_counter(globalVars.aux_type)


###################### M A K I N G    Q U A D R U P L E S ######################
def p_np_quad_a1_int(t):
    'np_quad_a1_int : empty'
    # int
    # grab the operand, since we have the type, we request an assigned space on memory
    # push type on stack
    constant_value = t[-1]
    constant_mem.save_memory_value(constant_value, 0)
    mem_act = constant_mem.get_counter(0)
    alg_quad.push_operand(mem_act)
    alg_quad.push_type(0)

def p_np_quad_a1_flt(t):
    'np_quad_a1_flt : empty'
    # float
    # grab the operand, since we have the type, we request an assigned space on memory
    # push type on stack
    constant_value = t[-1]
    constant_mem.save_memory_value(constant_value, 1)
    mem_act = constant_mem.get_counter(1)
    alg_quad.push_operand(mem_act)
    alg_quad.push_type(1)

def p_np_quad_a1_chr(t):
    'np_quad_a1_chr : empty'
    # char
    # grab the operand, since we have the type, we request an assigned space on memory
    # push type on stack
    constant_value = t[-1]
    constant_mem.save_memory_value(constant_value, 2)
    mem_act = constant_mem.get_counter(2)
    alg_quad.push_operand(mem_act)
    alg_quad.push_type(2)

def p_np_quad_a1_str(t):
    'np_quad_a1_str : empty'
    # string
    # grab the operand, since we have the type, we request an assigned space on memory
    # push type on stack
    constant_value = t[-1]
    constant_mem.save_memory_value(constant_value, 3)
    mem_act = constant_mem.get_counter(3)
    alg_quad.push_operand(mem_act)
    alg_quad.push_type(3)

def p_np_quad_a1_bol(t):
    'np_quad_a1_bol : empty'
    # bool
    # grab the operand, since we have the type, we request an assigned space on memory
    # push type on stack
    constant_value = t[-1]
    # M was here. Saving the actual boolean rather than a string
    if constant_value == "True":
      constant_value = True
    else:
      constant_value = False

    constant_mem.save_memory_value(constant_value, 4)
    mem_act = constant_mem.get_counter(4)
    alg_quad.push_operand(mem_act)
    alg_quad.push_type(4)

def p_np_quad_a2(t):
    'np_quad_a2 : empty'
    # Get the id from the variable
    id_var = t[-1]
    globalVars.aux_ID = id_var

    # Check if the "id" exists in the global variable table
    if globalVars.variable_in_global(id_var) :
        function_table = globalVars.table_functions[globalVars.global_context]
        var_table = function_table.vars_table[id_var]
        # Capture the value of the "memory ID" assigned to that variable
        temp_memID = var_table.direction
        # Capture the value of the "type" that belongs to that variable
        temp_type = var_table.type
        # Change the type to its equivalent integer
        temp_type = type_conv.get(temp_type)
        # Store the values "memory ID" and "type" in the corresponding stacks
        #   of the "alg_quad" object
        alg_quad.push_operand(temp_memID)
        alg_quad.push_type(temp_type)

    # If it doesn't exist as global. Check if the "id" exists in the local variable table
    elif globalVars.variable_in_local(id_var) :
        function_table = globalVars.table_functions[globalVars.current_context]
        var_table = function_table.vars_table[id_var]
        # Capture the value of the "memory ID" assigned to that variable
        temp_memID = var_table.direction
        # Capture the value of the "type" that belongs to that variable
        temp_type = var_table.type
        # Change the type to its equivalent integer
        temp_type = type_conv.get(temp_type)
        # Store the values "memory ID" and "type" in the corresponding stacks
        #   of the "alg_quad" object
        alg_quad.push_operand(temp_memID)
        alg_quad.push_type(temp_type)

    # The variable specified was not declared
    else:
        print ('ERROR: Variable: <{0}>, in function: <{1}> was not declared'.format(id_var, globalVars.current_context));
        p_error(t)

def p_np_quad_b(t):
    'np_quad_b : empty'
    # grab the operand and place it on the stack
    # convert operand into its numeric value
    current_operator = operator_conv.get(t[-1])
    alg_quad.push_operator(current_operator)

def p_np_quad_c0(t):
    'np_quad_c0 : empty'
    # leaving current exp lvl, we check if we have a current level rule pending. if so, take out and resolve
    # checking + -
    peek_o = alg_quad.peek_operator()
    opAND = operator_conv.get('&&')
    opOR = operator_conv.get('||')

    if (peek_o == opAND or peek_o == opOR):
        # saves the operands
        operand_right = alg_quad.pop_operand()
        operand_left = alg_quad.pop_operand()
        # saves the operator
        op = alg_quad.pop_operator()
        # saves the types of the operation
        type_right = alg_quad.pop_type()
        type_left = alg_quad.pop_type()
        # check new type. if result is not "-1", then types match
        n_type = consult(op, type_left, type_right)

        if (n_type != -1):
            # new temp based on oracle
            temporal_mem.save_memory_value("", n_type)
            n_temp = temporal_mem.get_counter(n_type)
            alg_quad.add_quadruple(op, operand_left, operand_right, n_temp)
            alg_quad.push_operand(n_temp)
            alg_quad.push_type(n_type)
        else:
            sys.exit("ERROR: type mismatch")


def p_np_quad_c1(t):
    'np_quad_c1 : empty'
    # leaving current exp lvl, we check if we have a current level rule pending. if so, take out and resolve
    # checking + -
    peek_o = alg_quad.peek_operator()
    opLESST = operator_conv.get('<')
    opMORET = operator_conv.get('>')
    opLESSEQUAL = operator_conv.get('<=')
    opMOREEQUAL = operator_conv.get('>=')
    opEQUALTO = operator_conv.get('==')
    opNOTEQUALTO = operator_conv.get('!=')


    if (peek_o == opLESST or peek_o == opMORET or peek_o == opLESSEQUAL or peek_o == opMOREEQUAL or peek_o == opEQUALTO or peek_o == opNOTEQUALTO):
        # saves the operands
        operand_right = alg_quad.pop_operand()
        operand_left = alg_quad.pop_operand()
        # saves the operator
        op = alg_quad.pop_operator()
        # saves the types of the operation
        type_right = alg_quad.pop_type()
        type_left = alg_quad.pop_type()
        # check new type. if result is not "-1", then types match
        n_type = consult(op, type_left, type_right)

        if (n_type != -1):
            # new temp based on oracle
            temporal_mem.save_memory_value("", n_type)
            n_temp = temporal_mem.get_counter(n_type)
            alg_quad.add_quadruple(op, operand_left, operand_right, n_temp)
            alg_quad.push_operand(n_temp)
            alg_quad.push_type(n_type)
        else:
            sys.exit("ERROR: type mismatch")

def p_np_quad_c2(t):
    'np_quad_c2 : empty'
    # leaving current exp lvl, we check if we have a current level rule pending. if so, take out and resolve
    # checking + -
    peek_o = alg_quad.peek_operator()
    opADD = operator_conv.get('+')
    opSUB = operator_conv.get('-')

    if (peek_o == opADD or peek_o == opSUB):
        # saves the operands
        operand_right = alg_quad.pop_operand()
        operand_left = alg_quad.pop_operand()
        # saves the operator
        op = alg_quad.pop_operator()
        # saves the types of the operation
        type_right = alg_quad.pop_type()
        type_left = alg_quad.pop_type()
        # check new type. if result is not "-1", then types match
        n_type = consult(op, type_left, type_right)

        if (n_type != -1):
            # new temp based on oracle
            temporal_mem.save_memory_value("", n_type)
            n_temp = temporal_mem.get_counter(n_type)
            alg_quad.add_quadruple(op, operand_left, operand_right, n_temp)
            alg_quad.push_operand(n_temp)
            alg_quad.push_type(n_type)
        else:
            sys.exit("ERROR: type mismatch")


def p_np_quad_c3(t):
    'np_quad_c3 : empty'
    # leaving current exp lvl, we check if we have a current level rule pending. if so, take out and resolve
    # checking * / %
    peek_o = alg_quad.peek_operator()
    opDIV = operator_conv.get('/')
    opMUL = operator_conv.get('*')
    opMOD = operator_conv.get('%')

    if (peek_o == opDIV or peek_o == opMUL or peek_o == opMOD):
        operand_right = alg_quad.pop_operand()
        operand_left = alg_quad.pop_operand()
        op = alg_quad.pop_operator()
        t_right = alg_quad.pop_type()
        t_left = alg_quad.pop_type()
        # check new type. if -1, type mis match
        n_type = consult(op, t_left, t_right)
        if (n_type != -1):
            # new temp based on oracle
            temporal_mem.save_memory_value("", n_type)
            n_temp = temporal_mem.get_counter(n_type)
            alg_quad.add_quadruple(op, operand_left, operand_right, n_temp)
            alg_quad.push_operand(n_temp)
            alg_quad.push_type(n_type)
        else:
            sys.exit("ERROR: type mismatch")

def p_np_quad_c4(t):
    'np_quad_c4 : empty'
    # leaving current exp lvl, we check if we have a current level rule pending. if so, take out and resolve
    # checking + -
    peek_o = alg_quad.peek_operator()
    opNOT = operator_conv.get('!')

    if (peek_o == opNOT):
        # saves the operands
        operand_right = alg_quad.pop_operand()
        # saves the operator
        op = alg_quad.pop_operator()
        # saves the types of the operation
        type_right = alg_quad.pop_type()
        # check new type. if result is not "-1", then types match
        n_type = consult(op, type_right, 4)

        if (n_type != -1):
            # new temp based on oracle
            temporal_mem.save_memory_value("", n_type)
            n_temp = temporal_mem.get_counter(n_type)
            alg_quad.add_quadruple(op, operand_right, "", n_temp)
            alg_quad.push_operand(n_temp)
            alg_quad.push_type(n_type)
        else:
            sys.exit("ERROR: type mismatch")

def p_np_quad_d1(t):
    'np_quad_d1 : empty'
    id_var = globalVars.aux_ID
    # found a dimensional variable. need to extract the O stack and transform into actual mem loc
    useless_operand = alg_quad.pop_operand()
    # useless_operand = alg_quad.peek_operand()

    # Check if the "id" exists in the global variable table
    if globalVars.variable_in_global(globalVars.aux_ID) :
        dim_description = globalVars.table_functions[globalVars.global_context].vars_table[globalVars.aux_ID].dimension


    # If it doesn't exist as global. Check if the "id" exists in the local variable table
    elif globalVars.variable_in_local(id_var) :
        dim_description = globalVars.table_functions[globalVars.current_context].vars_table[globalVars.aux_ID].dimension

    alg_quad.push_dim({'id': useless_operand, 'dim': 1, 'desc': dim_description})

def p_np_quad_d2(t):
    'np_quad_d2 : empty'
    # found a dimensional variable. need to extract the O stack and transform into actual mem loc
    curr_operand = alg_quad.peek_operand()
    op_type = alg_quad.peek_type()
    curr_dim = alg_quad.peek_dim()
    if op_type == 0:
      alg_quad.add_quadruple('VERF', curr_operand, 0, curr_dim['desc']['sup'])
      if curr_dim['desc']['next']:
        curr_operand = alg_quad.pop_operand()
        op_type = alg_quad.pop_type()

        temporal_mem.save_memory_value("", op_type)
        n_temp = temporal_mem.get_counter(op_type)

        alg_quad.add_quadruple(2, curr_operand, "$"+str(int(curr_dim['desc']['aux'])), n_temp)
        alg_quad.push_operand(n_temp)
        alg_quad.push_type(op_type)

      if curr_dim['dim'] > 1:
        aux_1 = alg_quad.pop_operand()
        aux1_t = alg_quad.pop_type()

        aux_2 = alg_quad.pop_operand()
        aux2_t = alg_quad.pop_type()

        temporal_mem.save_memory_value("", aux1_t)
        n_temp = temporal_mem.get_counter(aux1_t)

        alg_quad.add_quadruple(0, aux_1, aux_2, n_temp)
        alg_quad.push_operand(n_temp)
        alg_quad.push_type(aux1_t)
    else:
      sys.exit("ERROR: Array access must be of type int")

def p_np_quad_d3(t):
    'np_quad_d3 : empty'
    # verify if the variable has a next dimension. if not, mark error
    curr_dim = alg_quad.pop_dim()
    if curr_dim['desc']['next']:
      curr_dim['desc'] = curr_dim['desc']['next']
      curr_dim['dim'] = 2
    else:
      sys.exit("ERROR: Array invalid access. Array isnt bi-dimensional")

    alg_quad.push_dim(curr_dim)

def p_np_quad_d4(t):
    'np_quad_d4 : empty'
    # found a dimensional variable. need to extract the O stack and transform into actual mem loc
    curr_operand = alg_quad.peek_operand()
    op_type = alg_quad.peek_type()
    curr_dim = alg_quad.peek_dim()
    if op_type == 0:
      alg_quad.add_quadruple('VERF', curr_operand, 0, curr_dim['desc']['sup'])

      if curr_dim['dim'] > 1:
        aux_1 = alg_quad.pop_operand()
        aux1_t = alg_quad.pop_type()

        aux_2 = alg_quad.pop_operand()
        aux2_t = alg_quad.pop_type()

        temporal_mem.save_memory_value("", aux1_t)
        n_temp = temporal_mem.get_counter(aux1_t)

        alg_quad.add_quadruple(0, aux_1, aux_2, n_temp)
        alg_quad.push_operand(n_temp)
        alg_quad.push_type(aux1_t)
    else:
      sys.exit("ERROR: Array access must be of type int")

def p_np_quad_d5(t):
    'np_quad_d5 : empty'
    # found a dimensional variable. need to extract the O stack and transform into actual mem loc
    curr_dim = alg_quad.pop_dim()
    if 'next' in curr_dim['desc']:
      if curr_dim['desc']['next']:
        sys.exit("ERROR: Array invalid access. Array is bi-dimensional and only one dimention was given")

    aux_1 = alg_quad.pop_operand()
    aux1_t = alg_quad.pop_type()

    temporal_mem.save_memory_value("", aux1_t)
    n_temp_1 = temporal_mem.get_counter(aux1_t)

    alg_quad.add_quadruple(0, aux_1, "$"+str(curr_dim['desc']['aux']), n_temp_1)

    temporal_mem.save_memory_value("", aux1_t)
    n_temp_2 = temporal_mem.get_counter(aux1_t)

    alg_quad.add_quadruple(0, n_temp_1, "$"+str(curr_dim['id']), n_temp_2)

    alg_quad.push_operand('('+str(n_temp_2)+')')
    alg_quad.push_type(aux1_t)


#---------------------------- p r i n t    q u a d -----------------------------
def p_np_quad_print(t):
    'np_quad_print : empty'
    # leaving current exp lvl, we check if we have a current level rule pending. if so, take out and resolve
    # checking + -
    peek_o = alg_quad.peek_operator()
    opPrint = operator_conv.get('print')

    if (peek_o == opPrint):
      # saves the operands
      # operand_right = alg_quad.pop_operand()
      operand_right = alg_quad.pop_operand()
      # saves the operator
      op = alg_quad.pop_operator()
      # saves the types of the operation
      type_right = alg_quad.pop_type()
      # check new type. if result is not "-1", then types match
      # n_type = consult(op, type_right, 4)
      # if (n_type != -1):
      # print not yet added to oracle
      # new temp based on oracle
      # n_temp = temporal_mem.get_counter(n_type)

      alg_quad.add_quadruple(op, operand_right, "", "")
      # things are consumed. not pushed back
      # alg_quad.push_operand(n_temp)
      # alg_quad.push_type(n_type)

#---------------------- a s s i g n a t i o n    q u a d -----------------------
def p_np_quad_assign(t):
    'np_quad_assign : empty'
    # leaving current exp lvl, we check if we have a current level rule pending. if so, take out and resolve
    # checking + -
    peek_o = alg_quad.peek_operator()
    op_assign = operator_conv.get('=')

    if (peek_o == op_assign):
        # saves the operands
        operand_right = alg_quad.pop_operand()
        operand_left = alg_quad.pop_operand()

        # saves the operator
        op = alg_quad.pop_operator()

        # saves the types of the operation
        type_right = alg_quad.pop_type()
        type_left = alg_quad.pop_type()

        # Checks if the types match with the oracle
        n_type = consult(op, type_left, type_right)

        if (n_type != -1):
            # Create the new cuadruple
            alg_quad.add_quadruple(op, operand_left, "", operand_right)
            # Change the "memory ID" of the left operand with the memory ID of the right operand
        else:
            sys.exit("ERROR: type mismatch")


####################### J U M P S   I N   S T A T U T E S ######################
#---------------------------- i f    -    e l s e ------------------------------
def p_np_statutes_a1(t):
    'np_statutes_a1 : empty'
    # Store the type previously obtained from the expression
    aux_type = alg_quad.peek_type()
    # If the type is boolean, then continue
    if aux_type == type_conv.get('bool'):
        # Pop the type and expression to make the quadruple
        aux_type = alg_quad.pop_type()
        aux_exp = alg_quad.pop_operand()
        # Add the IP to the "jump stack"
        alg_quad.push_jump(alg_quad.instruction_pointer)
        # Create a cuadruple with an empty GOTOF jump
        alg_quad.add_quadruple('GOTOF', aux_exp, '', '');
    # The type is not boolean, there is an error
    else:
      sys.exit("ERROR: Type mismatch in IF statement")

def p_np_statutes_a2(t):
    'np_statutes_a2 : empty'
    # When the IF statement is true, then we need to skip the ELSE section
    aux_jump = alg_quad.instruction_pointer
    alg_quad.add_quadruple('GOTO', '', '', '')
    # When the IF statement is false, we need to go back to fill the pending quadruple
    pending_jump = alg_quad.pop_jump()
    alg_quad.instruction_pointer = alg_quad.instruction_pointer + 1
    alg_quad.fill_jump(pending_jump)

    # Add the IP that has the  GOTO quadruple, previously generated
    alg_quad.push_jump(aux_jump)

def p_np_statutes_a3(t):
    'np_statutes_a3 : empty'
    pending_jump = alg_quad.pop_jump()
    alg_quad.fill_jump(pending_jump)

#--------------------------------- w h i l e -----------------------------------
def p_np_statutes_b1(t):
    'np_statutes_b1 : empty'
    # Add the current IP to the "jump stack"
    aux_ip = alg_quad.instruction_pointer
    alg_quad.push_jump(aux_ip)

def p_np_statutes_b2(t):
    'np_statutes_b2 : empty'
    # If the current type in the stack, is a boolean, then proceed
    if alg_quad.peek_type():
        # Save the current expression in the while
        aux_exp = alg_quad.pop_operand()
        # Save the current IP and add it to the "jump stack"
        aux_ip = alg_quad.instruction_pointer
        alg_quad.push_jump(aux_ip)
        # CReate the quadruple
        alg_quad.add_quadruple('GOTOF', aux_exp, '', '')
    # There is a type mismatch with the statement
    else:
        sys.exit("ERROR: Type mismatch in WHILE statement")

def p_np_statutes_b3(t):
    'np_statutes_b3 : empty'
    # Save the IP from the "jump stack" that takes to the end of the While
    aux_end_while = alg_quad.pop_jump()
    # Save the IP from the "jump stack" that takes to the beggining of the While
    aux_return_while = alg_quad.pop_jump()
    # Make the cuadruple to return to the beggining of the While expression
    alg_quad.add_quadruple('GOTO', '', '', aux_return_while+1)
    # Fill the pending quadruple with the jump to the end of the While expression
    alg_quad.instruction_pointer = alg_quad.instruction_pointer + 1
    alg_quad.fill_jump(aux_end_while)
    alg_quad.instruction_pointer = alg_quad.instruction_pointer - 1

#------------------------------ d o   w h i l e --------------------------------
def p_np_statutes_c1(t):
    'np_statutes_c1 : empty'
    aux_ip = alg_quad.instruction_pointer
    alg_quad.push_jump(aux_ip)

def p_np_statutes_c2(t):
    'np_statutes_c2 : empty'
    # If the current type in the stack, is a boolean, then proceed
    if alg_quad.peek_type():
        aux_jump = alg_quad.pop_jump()
        aux_exp = alg_quad.pop_operand()
        alg_quad.add_quadruple('GOTOV', aux_exp, '', aux_jump)
    # There is a type mismatch with the statement
    else:
        sys.exit("ERROR: Type mismatch in DO-WHILE statement")

#----------------------------------- f o r -------------------------------------
def p_np_statutes_d1(t):
    'np_statutes_d1 : empty'
    aux_ip = alg_quad.instruction_pointer
    alg_quad.push_jump(aux_ip)

def p_np_statutes_d2(t):
    'np_statutes_d2 : empty'
    if alg_quad.peek_type():
        # Save the current expression in the while
        aux_exp = alg_quad.pop_operand()
        # Save the current IP and add it to the "jump stack"
        aux_ip = alg_quad.instruction_pointer
        alg_quad.push_jump(aux_ip)
        # CReate the quadruple
        alg_quad.add_quadruple('GOTOF', aux_exp, '', '')

        #Create GOTO when true
        #Save the pointer
        aux_ip2 = alg_quad.instruction_pointer
        alg_quad.push_jump(aux_ip2)
        # CReate the quadruple
        alg_quad.add_quadruple('GOTO', '', '', '')

        # push jump for the begining of the assignation
        aux_ip3 = alg_quad.instruction_pointer
        alg_quad.push_jump(aux_ip3)
    else:
        sys.exit("ERROR: Type mismatch in FOR statement")

def p_np_statutes_d3(t):
    'np_statutes_d3 : empty'
    assig_jump = alg_quad.pop_jump()
    goto_jump = alg_quad.pop_jump()
    gotof_jump = alg_quad.pop_jump()
    start_jump = alg_quad.pop_jump()
    # Make the cuadruple to go directly t the evaluation of the expression of the FOR
    alg_quad.add_quadruple('GOTO', '', '', start_jump)
    # Since now we have the begining of the expression, we can fill out the goto jump
    alg_quad.fill_jump(goto_jump)
    # Push back in the start of assignation and gotof jump
    alg_quad.push_jump(gotof_jump)
    alg_quad.push_jump(assig_jump)

def p_np_statutes_d4(t):
    'np_statutes_d4 : empty'
    assig_jump = alg_quad.pop_jump()
    gotof_jump = alg_quad.pop_jump()
    # Create a GOTO for the beginign of the assignation
    alg_quad.add_quadruple('GOTO', '', '', assig_jump)
    #since now we now the end of the for, we can fill the gotof jump
    alg_quad.fill_jump(gotof_jump)

################################################################################
#                               F U N C T I O N                                #
################################################################################
def p_np_goto_main(t):
    'np_goto_main : empty'
    # Add the a pending jump to the "jump stack"
    alg_quad.push_jump(alg_quad.instruction_pointer)
    # Add the quadruple GOTO to skip to the main
    alg_quad.add_quadruple('GOTO', '', '', '')

def p_np_era(t):
    'np_era : empty'
    # Grab the current ID and verify if it is declared as a function.
    function_aux = t[-2]
    if function_aux in globalVars.table_functions:
      # If true, we save in the stack and create an ERA call
      alg_quad.push_function(function_aux)
      alg_quad.add_quadruple('ERA', function_aux, '', '')
    else:
      # else we kill
      print("\n" + "START DEBUGGER" + "\n");
      time.sleep(1.5);
      print("################# Tables ################")
      globalVars.print_tables()
      print()
      print("############### Quadruples ##############")
      alg_quad.print_quadruples()
      print()
      print("############ Stack Operators ############")
      alg_quad.print_operators()
      print()
      print("############ Stack Operands #############")
      alg_quad.print_operands()
      print("\n" + "END OF DEBBUGGER" + "\n");
      sys.exit("ERROR:  Function call to <" + str(function_aux) + "> does not exist")

def p_np_gosub(t):
    'np_gosub : empty'
    # We capture the value of the current amount of variables being sent to the function
    current_counter = alg_quad.param_counter + 1
    # Capture the number of paramters expected on the function
    paramters = globalVars.table_functions[alg_quad.peek_function()].get_parameter_size()
    # If the number of parameters sent is less than what the function expects,
    # then display an error message
    if current_counter < paramters:
        print('ERROR: More arguments expected on function call <{0}>'.format(alg_quad.peek_function()))
    # Program is ready to be executed. We create a GOSUB with the name
    function_name = alg_quad.pop_function()
    alg_quad.add_quadruple('GOSUB', function_name, '', '')
    alg_quad.param_counter = 0

    
    # Procedures to assign the return value, if any, to a temporal
    # Retrieve the function object from the table of directions
    function_obj = globalVars.search_function(function_name)
    # If that function is different from void...
    if function_obj.type != "void":
      # Then it was declared as a global variable to return the result
      func_obj = globalVars.search_variable_by_id(function_name)
      func_address = func_obj.direction
      func_type = type_conv.get(func_obj.type)


      # new temp based on oracle
      temporal_mem.save_memory_value("", func_type)
      n_temp = temporal_mem.get_counter(func_type)
      # Add a cuadruple to assign the result of the function to a new temporal
      alg_quad.add_quadruple(4, n_temp, '', func_address)
      # Add the temporal and the type to the stacks
      alg_quad.push_operand(n_temp)
      alg_quad.push_type(func_type)
    

def p_np_param(t):
    'np_param : empty'
    # Retrieve the memory location of the specified parameter
    parameter = alg_quad.pop_operand()
    # Retrieve the type of the specified parameter
    type_param = alg_quad.pop_type()
    # Retrieve the ID of the function being called
    function_name = alg_quad.peek_function()
    # Check that the parameter counter is below the amount of parameters declared
    if alg_quad.param_counter < globalVars.table_functions[function_name].get_parameter_size():
        # Check that the parameter sent will match with the type stored in the table
        type_function = type_conv.get(globalVars.table_functions[function_name].parameters[alg_quad.param_counter])
        if type_param == type_function:
            # Create the counter
            argument_number = "param" + str(alg_quad.param_counter)
            alg_quad.add_quadruple('PARAM', parameter, '', argument_number)
            # Update the "parameters" counter in the Algorithm_Quadruple
            alg_quad.param_counter = 1 + alg_quad.param_counter
        else:
            print('ERROR: Type mismatch in arguments on function call <{0}>'.format(function_name))
    else:
        print('ERROR: Too many arguments on function call <{0}>. Ignoring the remaining arguments'.format(function_name))

def p_np_return(t):
  'np_return : empty'
  # The last operand added to the stack
  ret = alg_quad.pop_operand()
  # Build a cuadruple of return with the last operand added in the stack
  alg_quad.add_quadruple('RETURN', ret, '', '')


################################################################################
#                                                                              #
#                                 O T H E R S                                  #
#                                                                              #
################################################################################
def p_debug(t):
    'debug : empty'
    print("\n" + "START DEBUGGER" + "\n");
    time.sleep(1.5);
    print("################# Tables ################")
    globalVars.print_tables()
    print()
    print("############### Quadruples ##############")
    alg_quad.print_quadruples()
    print()
    print("############ Stack Operators ############")
    alg_quad.print_operators()
    print()
    print("############ Stack Operands #############")
    alg_quad.print_operands()
    print("\n" + "END OF DEBBUGGER" + "\n");

def p_np_eof(t):
    'np_eof : empty'
    # Since this is the end of our progrm, we need to run several commands to finilize everything.
    # create an 'end' quadruple
    alg_quad.add_quadruple('END', '', '', '')
     # Reset the "memory ID counter" from the "local memory"
    #local_mem.reset_cont()
    # Reseting the "memory ID counter" from "temporal memory"
    #temporal_mem.reset_cont()

def p_empty(p):
    'empty :'
    pass

def p_error(t):
    sys.exit("Ending program due to errors")


# Used in MAIN, reads the data from the command line
def read_from_console():
    while True:
        try:
            s = input('WOOF > ')   # Use raw_input on Python 2
            print ("\n");
        except EOFError:
            break
        # Compiler
        parser.parse(s)
        print()
        # Virtual Machine
        vm = Virtual_Machine(global_mem, local_mem, temporal_mem, constant_mem, globalVars, alg_quad)
        vm.start()
        print()
        # End of execution

# Used in MAIN, reads the data from a file written by the user until the command
# "END" is typed
def read_from_file():
    print ("Indique el nombre del archivo y su extension, escriba 'END' para terminar el programa: ")
    fileName = input('WOOF > ')

    while fileName != "END":
        fileName = "tests/" + fileName
        file = open(fileName,"r")

        # Compiler
        parser.parse(file.read())
        print()

        # Virtual Machine
        vm = Virtual_Machine(global_mem,
                             local_mem,
                             temporal_mem,
                             constant_mem,
                             globalVars,
                             alg_quad)
        vm.start()
        # End of execution
        print()

        print ("Indique el nombre del archivo y su extension, escriba 'END' para terminar el programa: ")
        fileName = input('WOOF > ')

################################################################################
#                                                                              #
#                            M A I N  P R O G R A M                            #
#                                                                              #
################################################################################
parser = yacc.yacc()
read_from_file()
