
#def main():
list1 = [ 1 , 1 , 1 , 2 , 3 , 2 , 1 , 23 , 43 , 54 , 4 , 5 ,65 , 67 , 76 , 54 , 34 , 2 , 4 ,5 , 6 , 6 , 6, 7 , 8 , 9] # Count() function as an attribute to count the number of times the numeral 6 occours in the list1
print(list1.count(6))


listSet = set()

for x in list1:
    listSet.add(x)

max =0;
for x in listSet:
    print(x,"   ",list1.count(x))

    if ( list1.count(x)> max):
        max = list1.count(x)


print(" max  "+ str(max))

