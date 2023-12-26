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

Dict = {1: 'Geeks', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

print(Dict)

print(Dict[1])
print(Dict[2])
print(Dict[3])

for i in Dict:
    print(Dict[i])
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks',4: 'name'}


# accessing a element using key
print("Accessing a element using key:")
print(Dict['name'])

# accessing a element using key
print("Accessing a element using key:")
print(Dict[1])

# Creating a Dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'San Francisco'}


# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(3))

for i in Dict:
    print(Dict.get(i))