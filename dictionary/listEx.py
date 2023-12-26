from collections import Counter

Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Creating a Dictionary
# with dict() method
Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)

myDict = {1: 'Geeks', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

print(Dict)

print(Dict[1])
print(Dict[2])
print(Dict[3])

for i in Dict:
    print(Dict[i])
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks',4: 'name'}

my_list2 = list(Dict.values())
my_list = list(Dict.values())
print (my_list2)

mikeset= set()

for x in my_list:
     mikeset.add(x)

my_list = list(mikeset)
for x in my_list:
    print(x,"   ",my_list2.count(x))