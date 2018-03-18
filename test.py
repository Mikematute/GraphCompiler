################################################################################
# Test File used for different tests.
# Random
# Not to be evaluated
################################################################################

# tests for oracle
# from oracle import consult
# print(consult(0,7,1))

# tests for memory class
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
global_Mem.print_counters()