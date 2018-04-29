from function import Function

class Table:

    def __init__(self):
        self.table_functions = {}
        self.current_context = ""
        self.global_context = ""
        self.aux_ID = ""
        self.aux_type = ""
        self.R = 1


    def exists_in_global(self):
        return self.table_functions[self.global_context].search_variable(self.aux_ID);

    def exists_in_local(self):
        return self.table_functions[self.current_context].search_variable(self.aux_ID);

    def variable_in_global(self, variable):
        return self.table_functions[self.global_context].search_variable(variable);

    def variable_in_local(self, variable):
        return self.table_functions[self.current_context].search_variable(variable);

    def add_var(self, mem):
        self.table_functions[self.current_context].add_var(self.aux_ID, self.aux_type, mem)

    def add_dir(self):
        self.table_functions[self.current_context] = Function(self.current_context, self.aux_type);

    def delete_dir(self, directory):
        del self.table_functions[directory]

    def print_tables(self):
        for function in self.table_functions:
            function_details = self.table_functions[function]
            print ("----------------------------------------")
            function_details.print_function()


    def search_function(self, function_name):
        # If the function exists in the table of functions
        if function_name in self.table_functions:
            # Then return the object of the function
            return self.table_functions[function_name]


    def search_variable_by_memory(self, value):
        # Search through all the tables
        for table in self.table_functions:
            # Search through all the variables in each table
            for variable in self.table_functions[table].vars_table:
                # See if the variable matches the value
                var_memory = self.table_functions[table].vars_table[variable].direction
                if value == var_memory:
                    return self.table_functions[table].vars_table[variable]

    def search_variable_by_id(self, value):
        # Search through all the tables
        for table in self.table_functions:
            # Search through all the variables in each table
            for variable in self.table_functions[table].vars_table:
                # See if the variable matches the value
                var_id = self.table_functions[table].vars_table[variable].id
                if value == var_id:
                    return self.table_functions[table].vars_table[variable]

    def reset_tables(self):
        self.table_functions = {}
        self.current_context = ""
        self.global_context = ""
        self.aux_ID = ""
        self.aux_type = ""

    def reset_dim(self):
        self.R = 1

