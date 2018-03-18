class Quadruple:
    def __init__(self, op=0, el1=0, el2=0, res=0):
        self.operation = op;
        self.element_1 = el1;
        self.element_2 = el2;
        self.result = res;

    def print_quadruple(self):
        print("Operator:\t" + str(self.operation) + "\n" +
              "Element 1:\t" + str(self.element_1) + "\n" +
              "Element 2:\t" + str(self.element_2) + "\n" +
              "Result:\t\t" + str(self.result));
