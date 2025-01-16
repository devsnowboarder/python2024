class Counter:
  def __init__(self, start, end):
    self.current=start
    self.end = end


  def __iter__(self):
    return self

  def __next__(self):
    if self.current > self.end:
      raise StopIteration
    else:
      self.current +=1
      return self.current -1


counter = Counter(3,10)
for item in counter:
    print(item)


