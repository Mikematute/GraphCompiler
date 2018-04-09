from variable import Variable

class Function:

    def __init__(self, name="", type=""):
        # The name of the function
        self.id = name
        # The return type of the function
        self.type  = type
        # The initial direction in the quadruple table
        self.init_direction = -1
        # Number of parameters
        self.parameters = []
        # Number of variables
        self.variables = 0
        # Number of temporal variables generated
        self.temporal = 0
        # The table of variables
        self.vars_table = {}

    def add_var(self, var_ID, var_type, var_direction):
        aux_var = Variable(var_ID, var_type, var_direction)
        self.vars_table[var_ID] = {'details' : aux_var}
        self.variables = len(self.vars_table)

    def add_parameter(self, type):
        self.parameters.append(type)

    def get_parameter_size(self):
        return len(self.parameters)

    def search_variable(self, variable):
        return variable in self.vars_table

    def print_function(self):
        print("ID        : " + self.id)
        print("TYPE      : " + self.type)
        print("DIRECTION : " + str(self.init_direction))
        print("PARAMETERS: " + str(self.get_parameter_size()))
        print("PARA_TYPE : " + str(self.parameters))
        print("VARIABLES : " + str(self.variables))
        print("TEMPORALS : " + str(self.temporal))
        print("VARS TABLE:")
        print('{0:20} {1:10} {2:10}'.format("ID", "TYPE", "DIRECTION"))
        for variable in self.vars_table:
            variable_details = self.vars_table[variable]['details']
            variable_details.print_variable()
