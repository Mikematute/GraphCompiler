from quadruple import Quadruple

class Algorithm_Quadruple:
    def __init__(self):
        self.lst_quadruples = []
        self.instruction_pointer = 0
        self.s_jump = []
        self.s_operator = []
        self.s_operand = []
        self.s_type = []
        self.avail = -1

    def add_quadruple(self, op, el1, el2, res):
        temp_quad = Quadruple(op, el1, el2, res)
        self.lst_quadruples.append(temp_quad)
        self.instruction_pointer += 1;


    def fill_jump(self, quad_location):
        self.lst_quadruples[quad_location].result = instruction_pointer

    def next_avail(self):
        self.avail += 1
        return self.avail

    # .print method
    # prints the value of the specified variable
    def print_quadruples(self):
        for quad in self.lst_quadruples:
            quad.print_quadruple();

    def print_jumps(self):
        for jump in self.s_jump:
            print(str(jump) + " ", end='')
        print()

    def print_operators(self):
        for operator in self.s_operator:
            print(str(operator) + " ", end='')
        print()

    def print_operands(self):
        for operand in self.s_operand:
            print(str(operand) + " ", end='')
        print()

    def print_types(self):
        for type in self.s_type:
            print(str(type) + " ", end='')
        print()


    # .push method
    # pushes the 'var' into the specified stack
    def push_jump(self, var):
        self.s_jump.append(var)

    def push_operator(self, var):
        self.s_operator.append(var)

    def push_operand(self, var):
        self.s_operand.append(var)

    def push_type(self, var):
        self.s_type.append(var)

    # .pop method
    # pops the first element form the specified stack
    def pop_jump(self):
        return self.s_jump.pop()

    def pop_operator(self):
        return self.s_operator.pop()

    def pop_operand(self):
        return self.s_operand.pop()

    def pop_type(self):
        return self.s_type.pop()

    # .peek method
    # returns the first element from the specified stack without poping it
    def peek_jump(self):
        return self.s_jump[-1]

    def peek_operator(self):
        return self.s_operator[-1]

    def peek_operand(self):
        return self.s_operand[-1]

    def peek_type(self):
        return self.s_type[-1]
