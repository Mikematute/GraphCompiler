class Tables:
    dicDirections = {};
    currentContext = "";
    globalContext = "";
    auxID = "";
    auxType = "";

    def __init__(self):
        dicDirections = {};
        currentContext = "";
        globalContext = "";
        auxID = "";
        auxType = "";

    def exists_in_global(self):
        return self.auxID in self.dicDirections[self.globalContext]['vars'];

    def exists_in_local(self):
        return self.auxID in self.dicDirections[self.currentContext]['vars'];
        #variable in self.dicDirections[self.currentContext]['vars'];

    def variable_in_global(self, variable):
        return variable in self.dicDirections[self.globalContext]['vars'];

    def variable_in_local(self, variable):
        return variable in self.dicDirections[self.currentContext]['vars'];

    def add_var(self, mem):
        self.dicDirections[self.currentContext]['vars'][self.auxID] = {'type': self.auxType, 'memory': mem};

    def add_dir(self):
        self.dicDirections[self.currentContext] = {'type': self.auxType};

    def delete_dir(self, directory):
        del self.dicDirections[directory]

    def print_tables(self):
        for direction in self.dicDirections:
            print(direction);
            print("\tType:" + self.dicDirections[direction]['type']);
            for varID in self.dicDirections[direction]['vars']:
                memory_ID = self.dicDirections[direction]['vars'][varID]['memory']
                print("\t\tVar: " + varID + "\t" + "Memory: " + str(memory_ID));
                #for varType in globalVars.dicDirections[direction]['vars'][varID]['type']:
                #    print("\t\tVar: " + varID + "\t" + "Type: " + varType);

    def reset_tables(self):
        self.currentContext = "";
        self.globalContext = "";
        self.auxID = "";
        self.auxType = "";
        self.dicDirections = {};
