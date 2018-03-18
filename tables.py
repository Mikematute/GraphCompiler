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

    def add_var(self):
        self.dicDirections[self.currentContext]['vars'][self.auxID] = {'type': self.auxType};

    def add_dir(self):
        self.dicDirections[self.currentContext] = {'type': self.auxType};

    def print_tables(self):
        for direction in self.dicDirections:
            print(direction);
            print("\tType:" + self.dicDirections[direction]['type']);
            for varID in self.dicDirections[direction]['vars']:
                print("\t\tVar: " + varID + "\t");
                #for varType in globalVars.dicDirections[direction]['vars'][varID]['type']:
                #    print("\t\tVar: " + varID + "\t" + "Type: " + varType);

    def reset_tables(self):
        self.currentContext = "";
        self.globalContext = "";
        self.auxID = "";
        self.auxType = "";
        self.dicDirections = {};
