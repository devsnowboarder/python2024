class Fabo:
    def __init__(self,max):
        self.max= max
        self.a = 0
        self.b = 1

    def  __iter__(self):
        self.a, self.b = 0 , 1
        return self

    def __next__(self):
        if self.a > self.max:
            raise StopIteration
        else:
          self.a, self.b = self.b , self.a + self.b
          return self.a - self.b

    def generate(self):
        while self.a <= self.max:
            yield self.a
            self.a, self.b = self.b , self.a + self.b


fib = Fabo(10)
for num in fib.generate():
    print(num)