################################################################################
# Test File used for different tests.
# Random
# Not to be evaluated
################################################################################

# tests for oracle
# from oracle import consult
# print(consult(0,7,1))

#--------------------------- tests for memory class ----------------------------
'''
from memory import Memory

print("Declaring Global memory")
global_Mem = Memory(1)
print("printing current counters for Global memorry")
global_Mem.print_counters()

print()
print("assigning a new float pos: ")
print(global_Mem.get_counter_id("float"))
print()
print("printing current counters for Global memorry")
global_Mem.print_counters
print()
'''

#------------------------- tests for quadruple class ---------------------------
'''
from quadruple import Quadruple
print("###################### QUADRUPLE TEST ######################")
print("Declaring Quadruple")
print("Printing empty constructor")
my_quad = Quadruple();
my_quad.print_quadruple();
print("Printing constructor with variables")
my_quad = Quadruple(1,2,3,4);
my_quad.print_quadruple();
print()
'''

#---------------------- tests for list_Quadruples class ------------------------
'''
from algorithmQuadruple import Algorithm_Quadruple
print("################# QUADRUPLE ALGORITHM TEST #################")
print("Declaring List of Quadruples")
print("Printing empty constructor")
my_quad_list = Algorithm_Quadruple();
my_quad_list.print_quadruples();
print("Printing list after adding elements")
my_quad_list.add_quadruple(1,2,3,4);
my_quad_list.add_quadruple(5,6,7,8);
my_quad_list.add_quadruple(9,0,1,2);
my_quad_list.print_quadruples();
print()
print("Printing jump stack")
my_quad_list.push_jump(11)
my_quad_list.push_jump(12)
my_quad_list.push_jump(13)
my_quad_list.push_jump(14)
my_quad_list.push_jump(15)
my_quad_list.print_jumps()
print("Printing operator stack")
my_quad_list.push_operator(21)
my_quad_list.push_operator(22)
my_quad_list.push_operator(23)
my_quad_list.push_operator(24)
my_quad_list.push_operator(25)
my_quad_list.print_operators()
print("Printing operand stack")
my_quad_list.push_operand(31)
my_quad_list.push_operand(32)
my_quad_list.push_operand(33)
my_quad_list.push_operand(34)
my_quad_list.push_operand(35)
my_quad_list.print_operands()
print("Printing type stack")
my_quad_list.push_type("int")
my_quad_list.push_type("float")
my_quad_list.push_type("char")
my_quad_list.push_type("string")
my_quad_list.push_type("bool")
my_quad_list.print_types()
print()
'''

#------------------------- Test Mike Shananigans ---------------------------
'''operand_conv = { '+': 0,
                  '-': 1,
                  '*': 2,
                  '/': 3,
                  '=': 4,
                  '%': 5,
                  '&&': 6,
                  '||': 7,
                  '<': 8,
                  '>': 9,
                  '<=': 10,
                  '>=': 11,
                  '!=': 12,
                  '==': 13,
                  '!': 14}

current_operand = operand_conv.get('<')
print(current_operand)
'''
'''
from memory import Memory
global_mem   = Memory(1)

dummy = global_mem.get_counter_id("int")
dummy = global_mem.get_counter_id("int")
dummy = global_mem.get_counter_id("int")
dummy = global_mem.get_counter_id("int")
dummy = global_mem.get_counter_id("undirected")
dummy = global_mem.get_counter_id("undirected")
dummy = global_mem.get_counter_id("directed")

print(global_mem.used_mem())
'''
#----------------------------- Test function tables ----------------------------
from table import Table
my_table = Table()
my_table.global_context = "cats"
my_table.current_context = "cats"
my_table.aux_type = "void"
my_table.add_dir()
my_table.aux_ID = "my_global1"
my_table.aux_type = "int"
my_table.add_var(1001)
my_table.aux_ID = "my_global2"
my_table.aux_type = "int"
my_table.add_var(1002)
my_table.aux_ID = "my_global3"
my_table.aux_type = "int"
my_table.add_var(1003)

my_table.current_context = "my_function"
my_table.aux_type = "double"
my_table.add_dir()
my_table.aux_ID = "my_local1"
my_table.aux_type = "float"
my_table.add_var(2001)
my_table.aux_ID = "my_local2"
my_table.aux_type = "double"
my_table.add_var(2002)
my_table.aux_ID = "my_local3"
my_table.aux_type = "bool"
my_table.add_var(2003)

my_table.current_context = "main"
my_table.aux_type = "void"
my_table.add_dir()
my_table.aux_ID = "hello"
my_table.aux_type = "char"
my_table.add_var(3001)
my_table.aux_ID = "there"
my_table.aux_type = "string"
my_table.add_var(3002)

my_table.print_tables()
