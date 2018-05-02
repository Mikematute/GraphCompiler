class Quadruple:
    def __init__(self, op=0, el1=0, el2=0, res=0):
        self.operation = op;
        self.element_1 = el1;
        self.element_2 = el2;
        self.result = res;

    '''
    def print_quadruple(self):
        print("Operator:\t" + str(self.operation) + "\n" +
              "Element 1:\t" + str(self.element_1) + "\n" +
              "Element 2:\t" + str(self.element_2) + "\n" +
              "Result:\t\t" + str(self.result));
        print()
    '''
    def print_quadruple(self):
        print(self.string_quadruple())

    def string_quadruple(self):
        op = str(self.operation)
        el_1 = str(self.element_1)
        el_2 = str(self.element_2)
        res = str(self.result)

        if el_1 == "" :
            el_1 = "-----"

        if el_2 == "" :
            el_2 = "-----"

        if res == "" :
            res = "-----"

        return '{0:10} {1:15} {2:10} {3:10}'.format(op, el_1, el_2, res)
