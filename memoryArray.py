class Memory_Array:

    def __init__(self, cont=0):
        self.counter = cont
        self.values = []

    def get_value(self, index):
        return self.values[index]

    def add_value(self, value):
        self.values.append(value)

    def add_value_at_index(self, value, index):
        self.values[index] = value

    def increment_counter(self, increment=1):
        self.counter = self.counter + increment

