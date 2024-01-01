class Address:
  def __init__(mine, street, number):
    mine.street = street
    mine.number = number

  def myfunc(addressInfo):
    print("My Address is " + addressInfo.street)
    print(" My number is " + str(addressInfo.number))


class MyName:

  def _init_(self, Nathan):
    self.name = Nathan

  def my_name(self):
    return self.name


p1 = Address("Albert Street", 20)
p1.myfunc()
p2 = MyName()





#ppInfo.my_name()