class Variable:

    def __init__(self, var_ID="", var_type="", var_direction=-1):
        # The name of the variable
        self.id = var_ID
        # The return type of the function
        self.type  = var_type
        # The direction in the memory
        self.direction = var_direction

    def print_variable(self):
        print('{0:20} {1:10} {2:10}'.format(self.id, self.type, self.direction))
