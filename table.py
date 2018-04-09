from function import Function

class Table:

    def __init__(self):
        self.table_functions = {}
        self.current_context = ""
        self.global_context = ""
        self.aux_ID = ""
        self.aux_type = ""

    def exists_in_global(self):
        return self.table_functions[self.global_context]['details'].search_variable(self.aux_ID);

    def exists_in_local(self):
        return self.table_functions[self.local_context]['details'].search_variable(self.aux_ID);

    def variable_in_global(self, variable):
        return self.table_functions[self.global_context]['details'].search_variable(variable);

    def variable_in_local(self, variable):
        return self.table_functions[self.local_context]['details'].search_variable(variable);

    def add_var(self, mem):
        self.table_functions[self.current_context]['details'].add_var(self.aux_ID, self.aux_type, mem)

    def add_dir(self):
        self.table_functions[self.current_context] = {'details': Function(self.current_context, self.aux_type)};

    def delete_dir(self, directory):
        del self.table_functions[directory]

    def print_tables(self):
        for function in self.table_functions:
            function_details = self.table_functions[function]['details']
            print ("----------------------------------------")
            function_details.print_function()

    def reset_tables(self):
        self.table_functions = {}
        self.current_context = ""
        self.global_context = ""
        self.aux_ID = ""
        self.aux_type = ""
