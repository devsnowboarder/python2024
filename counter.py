from collections import Counter
a = [1,1,1,1,2,3,3,4,3,3,4]
c = Counter(a)

Maxcount = max(c)
print(c)

print(Maxcount)

setList =set()

for x in a:
    setList.add(x)

print(setList)

print(a.count(1))

for x in setList:
   if  a.count(x) > 1:
       print(" duplicate number  "+str(x))