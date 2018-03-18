################################################################################
# Test File used for different tests.
# Random
# Not to be evaluated
################################################################################

# tests for oracle
# from oracle import consult
# print(consult(0,7,1))

#--------------------------- tests for memory class ----------------------------
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

#------------------------- tests for quadruple class ---------------------------
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

#---------------------- tests for list_Quadruples class ------------------------
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
