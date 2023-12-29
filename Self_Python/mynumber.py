class mynumber:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)


class Subject:

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

obj1 = mynumber(17)
obj1.print_value()

obj = Subject('Maths', 'Science')
print(obj.attr1)
print(obj.attr2)