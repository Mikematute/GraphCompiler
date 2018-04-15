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
            self.perform_operation(current_quad)
            current_quad = self.quadruples.lst_quadruples[self.instruction_pointer]

    def perform_operation(self, quad):
        operation = quad.operation
        #--------------------------- a d d i t i o n ---------------------------
        if operation == 0:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op + r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------ s u b s t r a c t i o n ----------------------
        if operation == 1:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op - r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #---------------------------- p r o d u c t ----------------------------
        if operation == 2:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op * r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #--------------------------- d i v i s i o n ---------------------------
        if operation == 3:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op / r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------- a s s i g n a t i o n -----------------------
        if operation == 4:
            # Get the left operator
            memory_id = quad.element_1
            # Get the right operator
            value = self.search_in_memory(quad.result)
            # Cast the result into the appropiate type according to the oracle
            # Save the result in the left operator
            self.save_in_memory(memory_id, value)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #----------------------------- m o d u l o -----------------------------
        if operation == 5:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op % r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #-------------------------------- a n d --------------------------------
        if operation == 6:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op and r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #--------------------------------- o r ---------------------------------
        if operation == 7:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op or r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------- l e s s    t h a n --------------------------
        if operation == 8:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op < r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------- m o r e    t h a n --------------------------
        if operation == 9:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op > r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------ l e s s  e q  t h a n ------------------------
        if operation == 10:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op <= r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------ m o r e  e q  t h a n ------------------------
        if operation == 11:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op >= r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #-------------------------- d i f f e r e n t --------------------------
        if operation == 12:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op != r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------------ e q u a l ------------------------------
        if operation == 13:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Get the right operator
            r_op = self.search_in_memory(quad.element_2)
            # Perform the operation
            result = l_op == r_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #-------------------------------- n o t --------------------------------
        if operation == 14:
            # Get the left operator
            l_op = self.search_in_memory(quad.element_1)
            # Perform the operation
            result = not l_op
            # Cast the result into the appropiate type according to the oracle
            result = self.cast_to_type(quad, result)
            # Save the result in the temporal specified
            self.save_in_memory(quad.result, result)
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------------ p r i n t ------------------------------
        elif operation == 15:
            # Get the operator
            l_op = self.search_in_memory(quad.element_1)
            # Perform the operation
            print(str(l_op))
            # Advance the instruction pointer one step
            self.instruction_pointer = self.instruction_pointer + 1
        #------------------------------- g o t o -------------------------------
        elif operation == 'GOTO':
            # Skip the instruction pointer to the number indicated
            self.instruction_pointer = quad.result - 1
        #------------------------------ g o t o v ------------------------------
        elif operation == 'GOTOV':
            # Get the boolean expression
            l_op = self.search_in_memory(quad.element_1)
            # Evaluate if the expression is TRUE
            result = l_op == True
            # If the expression is TRUE then move the instruction pointer to the
            # specified jump in the result field (indicated in the quadruple)
            if result:
                self.instruction_pointer = quad.result - 1
            else:
                self.instruction_pointer = self.instruction_pointer + 1
        #------------------------------ g o t o f ------------------------------
        elif operation == 'GOTOF':
            # Get the boolean expression
            l_op = self.search_in_memory(quad.element_1)
            # Evaluate if the expression is FLASE
            result = l_op == False
            # If the expression is FLASE then move the instruction pointer to the
            # specified jump in the result field (indicated in the quadruple)
            if result:
                self.instruction_pointer = quad.result - 1
            else:
                self.instruction_pointer = self.instruction_pointer + 1
        #-------------------------------- e r a --------------------------------
        #------------------------------ p a r a m ------------------------------
        #------------------------------ g o s u b ------------------------------
        #----------------------------- r e t u r n -----------------------------

    def search_in_memory(self, memory_id):
        # Obtains the first digit to know which memory the ID belongs to
        memory_type = int(memory_id / 10000)

        # If the result is 1, it is the global memory
        if memory_type == 1:
            return self.global_mem.get_memory_value(memory_id)
        # If the result is 2, it is the local memory
        elif memory_type == 2:
            return self.local_mem.get_memory_value(memory_id)
        # If the result is 3, it is the temporal memory
        elif memory_type == 3:
            return self.temporal_mem.get_memory_value(memory_id)
        # If the result is 4, it is the constant memory
        elif memory_type == 4:
            return self.constant_mem.get_memory_value(memory_id)


    def save_in_memory(self, memory_id, result):
        memory_type = int(memory_id / 10000)

        # If the result is 1, then save the result in the global memory
        if memory_type == 1:
            self.global_mem.save_to_memory(result, memory_id)
        # If the result is 2, then save the result in the local memory
        elif memory_type == 2:
            self.local_mem.save_to_memory(result, memory_id)
        # If the result is 3, then save the result in the temporal memory
        elif memory_type == 3:
            self.temporal_mem.save_to_memory(result, memory_id)
        # If the result is 4, then save the result in the constant memory
        elif memory_type == 4:
            self.constant_mem.save_to_memory(result, memory_id)


    def cast_to_type(self, quadruple, value):
        '''
        # Retrive the type of the left operand involved in the operation
        type_left = quadruple.element_1
        type_left = self.globalVars.search_variable_by_memory(type_left)
        type_left = type_left.type
        # Retrive the type of the right operand involved in the operation
        type_right = quadruple.element_2
        type_right = self.globalVars.search_variable_by_memory(type_right)
        type_right = type_right.type
        # Retrieve the operation being performed
        operation = quadruple.operation
        # Consult the oracle to get the type of the result
        result_type = consult(operation, type_left, type_right)
        '''
        memory_type = int(quadruple.result / 10000)
        data_type = quadruple.result - (memory_type * 10000)
        data_type = int(data_type / 1000)
        result_type = data_type

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
