from table import Table
from oracle import consult
from memory import Memory
from algorithmQuadruple import Algorithm_Quadruple

class Virtual_Machine:
    def __init__(self, g_mem = Memory(1), l_mem = Memory(2), t_mem = Memory(3),
                c_mem = Memory(4), g_vars = Table(), quad = Algorithm_Quadruple()):
        self.global_mem     = g_mem
        self.local_mem      = l_mem
        self.temporal_mem   = t_mem
        self.constant_mem   = c_mem
        self.globalVars     = g_vars
        self.quadruples     = quad
        self.instruction_pointer = 0
        self.int_to_operator = { 0 : '+',
                                 1 : '-',
                                 2 : '*',
                                 3 : '/',
                                 4 : '=',
                                 5 : '%',
                                 6 : '&&',
                                 7 : '||',
                                 8 : '<',
                                 9 : '>',
                                10 : '<=',
                                11 : '>=',
                                12 : '!=',
                                13 : '==',
                                14 : '!',
                                15 : 'print'}



    def start(self):
        print("Starting VM")
        # Start "instruction_pointer" on 0
        self.instruction_pointer = 0
        # Save the the instruction located in the quadruple by the "instruction_pointer"
        current_quad = self.quadruples.lst_quadruples[self.instruction_pointer]

        # Read the quadruples until there is one with the "END" instruction
        while(current_quad.operation != "END"):
            current_quad.print_quadruple()
            self.perform_operation(current_quad)
            current_quad = self.quadruples.lst_quadruples[self.instruction_pointer]

    def perform_operation(self, quad):
        operation = quad.operation
        # If the operation is an integer between 0 and 15, then convert it to string
        if 0 <= operation and operation <= 15:
            operation = int_to_operator.get(operation)

        #--------------------------- a d d i t i o n ---------------------------
        if operation == '+':
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op + r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------ s u b s t r a c t i o n ----------------------
        #---------------------------- p r o d u c t ----------------------------
        #--------------------------- d i v i s i o n ---------------------------
        #------------------------- a s s i g n a t i o n -----------------------
        #----------------------------- m o d u l o -----------------------------
        #-------------------------------- a n d --------------------------------
        #--------------------------------- o r ---------------------------------
        #------------------------- l e s s    t h a n --------------------------
        #------------------------- m o r e    t h a n --------------------------
        #------------------------ l e s s  e q  t h a n ------------------------
        #------------------------ m o r e  e q  t h a n ------------------------
        #-------------------------- d i f f e r e n t --------------------------
        #------------------------------ e q u a l ------------------------------
        #-------------------------------- n o t --------------------------------
        #------------------------------ p r i n t ------------------------------
        elif operation == 'print':
            # Get the operator
            l_op = self.search_in_memory(quad.element_1)
            # Perform the operation
            print(str(l_op))
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1

    def search_in_memory(self, memory_id):
        # Code
        return 1

    def save_in_memory(self, result):
        # Code
        return 1

    def cast_to_type(self, quadruple, value):
        # Retrive the type of the left operand involved in the operation
        type_left = quadruple.element_1
        type_left = globalVars.search_variable_by_memory(type_left)
        type_left = type_left.type
        # Retrive the type of the right operand involved in the operation
        type_right = quadruple.element_2
        type_right = globalVars.search_variable_by_memory(type_right)
        type_right = type_right.type
        # Retrieve the operation being performed
        operation = quadruple.operation
        # Consult the oracle to get the type of the result
        result_type = consult(operation, type_left, type_right)
        # Return the result casted to that type
        if result_type == 0:
            return int(value)
        elif result_type == 1:
            return float(value)
        elif result_type == 2:
            return chr(value)
        elif result_type == 3:
            return str(value)
        elif result_type == 4:
            return bool(value)
