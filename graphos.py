################################################################################
#                         G L O B A L  H A N D L E R S                         #
################################################################################

from table import Table
from oracle import consult
from memory import Memory
from algorithmQuadruple import Algorithm_Quadruple
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
t_CTE_BOO =     r'True|False'
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
    'assignation : ID np_quad_a2 EQL np_quad_b expression np_quad_assign SCOLO'

#------------------------------- w r i t i n g ---------------------------------
def p_writing(t):
    'writing : PRINT np_quad_b LPAREN writing_1 RPAREN np_quad_print SCOLO'

def p_writing_1(t):
    '''writing_1 : expression
                 | CTE_STRING np_quad_a1_str
                 | writing_2'''

def p_writing_2(t):
    '''writing_2 : expression SUMA np_quad_b writing_1 np_quad_c2
                 | CTE_STRING np_quad_a1_str SUMA np_quad_b writing_1 np_quad_c2'''
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
               | method
               | ID np_quad_a2
               | ID np_quad_a2 array_access'''

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
    '''var_cte : CTE_INT np_quad_a1_int
               | CTE_FLO np_quad_a1_flt
               | CTE_BOO np_quad_a1_bol
               | CTE_STRING np_quad_a1_str
               | CTE_CHAR np_quad_a1_chr'''
    # print("enters cons")

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
    globalVars.global_context = t[-1];
    # Stablish the current context to global
    globalVars.current_context = globalVars.global_context;
    # Add the ID to the directions table with its details
    globalVars.aux_type = "void";
    globalVars.add_dir();

def p_np_var_a2(t):
    'np_var_a2 : empty'
    # Create the table of global variables
    globalVars.table_functions[globalVars.global_context]

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

def p_np_var_b4(t):
    'np_var_b4 : empty'
    # Saves the variable type
    globalVars.aux_type = t[-1];

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
                temp_memID = global_mem.get_counter_id(globalVars.aux_type)
            else:
                # ... then ask for a "memory id" from the "local memory"
                temp_memID = local_mem.get_counter_id(globalVars.aux_type)

            # Adds a new entry to the table
            globalVars.add_var(temp_memID);
        else:
            print ('ERROR: Variable: <{0}>, in function: <{1}> already declared'.format(globalVars.aux_ID, globalVars.current_context));
            p_error(t)
    else:
        print ('ERROR: Variable: <{0}>, in function: <{1}> already declared as global'.format(globalVars.aux_ID, globalVars.current_context));
        p_error(t)

def p_np_var_b6(t):
    'np_var_b6 : empty'
    # Erease the current vars-table
    globalVars.delete_dir(globalVars.current_context)
    # Reset the "memory ID counter" from the "local memory"
    local_mem.reset_cont()
    # Reseting the "memory ID counter" from "temporal memory"
    temporal_mem.reset_cont()
    # We also need to add the end of the function quadruple.
    alg_quad.add_quadruple('RETURN', '', '', '')

#---------------------------------- m a i n ------------------------------------
def p_np_var_c1(t):
    'np_var_c1 : empty'
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
                temp_memID = global_mem.get_counter_id(globalVars.aux_type)
            else:
                # ... then ask for a "memory id" from the "local memory"
                temp_memID = local_mem.get_counter_id(globalVars.aux_type)

            # Adds a new entry to the table
            globalVars.add_var(temp_memID);
        else:
            print ('ERROR: Variable: <{0}>, in function: <{1}> already declared'.format(globalVars.aux_ID, globalVars.current_context));
            p_error(t)
    else:
        print ('ERROR: Variable: <{0}>, in function: <{1}> already declared as global'.format(globalVars.aux_ID, globalVars.current_context));
        p_error(t)

###################### M A K I N G    Q U A D R U P L E S ######################
def p_np_quad_a1_int(t):
    'np_quad_a1_int : empty'
    # int
    # grab the operand, since we have the type, we request an assigned space on memory
    # push type on stack

    mem_act = constant_mem.get_counter_num(0)
    alg_quad.push_operand(mem_act)
    alg_quad.push_type(0)

def p_np_quad_a1_flt(t):
    'np_quad_a1_flt : empty'
    # float
    # grab the operand, since we have the type, we request an assigned space on memory
    # push type on stack

    mem_act = constant_mem.get_counter_num(1)
    alg_quad.push_operand(mem_act)
    alg_quad.push_type(1)

def p_np_quad_a1_chr(t):
    'np_quad_a1_chr : empty'
    # char
    # grab the operand, since we have the type, we request an assigned space on memory
    # push type on stack

    mem_act = constant_mem.get_counter_num(2)
    alg_quad.push_operand(mem_act)
    alg_quad.push_type(2)

def p_np_quad_a1_str(t):
    'np_quad_a1_str : empty'
    # string
    # grab the operand, since we have the type, we request an assigned space on memory
    # push type on stack

    mem_act = constant_mem.get_counter_num(3)
    alg_quad.push_operand(mem_act)
    alg_quad.push_type(3)

def p_np_quad_a1_bol(t):
    'np_quad_a1_bol : empty'
    # bool
    # grab the operand, since we have the type, we request an assigned space on memory
    # push type on stack

    mem_act = constant_mem.get_counter_num(4)
    alg_quad.push_operand(mem_act)
    alg_quad.push_type(4)

def p_np_quad_a2(t):
    'np_quad_a2 : empty'
    # Get the id from the variable
    id_var = t[-1]

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
            n_temp = temporal_mem.get_counter_num(n_type)
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
            n_temp = temporal_mem.get_counter_num(n_type)
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
            n_temp = temporal_mem.get_counter_num(n_type)
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
            n_temp = temporal_mem.get_counter_num(n_type)
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
            n_temp = temporal_mem.get_counter_num(n_type)
            alg_quad.add_quadruple(op, operand_right, "", n_temp)
            alg_quad.push_operand(n_temp)
            alg_quad.push_type(n_type)
        else:
            sys.exit("ERROR: type mismatch")

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
      # n_temp = temporal_mem.get_counter_num(n_type)

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
    alg_quad.add_quadruple('GOTO', '', '', aux_return_while)
    # Fill the pending quadruple with the jump to the end of the While expression
    alg_quad.fill_jump(aux_end_while)

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
#                                 O T H E R S                                  #
################################################################################
def p_debug(t):
    'debug : empty'
    print("\n" + "START DEBUGGER" + "\n");
    time.sleep(1.5);
    print("######## Tables ########")
    globalVars.print_tables()
    print()
    print("###### Quadruples ######")
    alg_quad.print_quadruples()
    print()
    print("###### stack operators ######")
    alg_quad.print_operators()
    print()
    print("###### stack operands ######")
    alg_quad.print_operands()
    print("\n" + "END OF DEBBUGGER" + "\n");

def p_np_eof(t):
    'np_eof : empty'
    # Since this is the end of our progrm, we need to run several commands to finilize everything.
    # create an 'end' quadruple
    alg_quad.add_quadruple('END', '', '', '')
     # Reset the "memory ID counter" from the "local memory"
    local_mem.reset_cont()
    # Reseting the "memory ID counter" from "temporal memory"
    temporal_mem.reset_cont()


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
        parser.parse(s)

# Used in MAIN, reads the data from a file written by the user until the command
# "END" is typed
def read_from_file():
    print ("Indique el nombre del archivo y su extension, escriba 'END' para terminar el programa: ")
    fileName = input('WOOF > ')

    while fileName != "END":
        file = open(fileName,"r")
        parser.parse(file.read())
        print ("Indique el nombre del archivo y su extension, escriba 'END' para terminar el programa: ")
        fileName = input('WOOF > ')

################################################################################
#                            M A I N  P R O G R A M                            #
################################################################################
parser = yacc.yacc()
read_from_file()
