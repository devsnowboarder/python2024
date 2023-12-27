# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Adding elements one at a time
Dict[0] = 'Geeks'
Dict[1] = 'For'
Dict[2] = 'Geeks'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

mylist=list()

for  keys in Dict.values():
    print(keys)
    mylist.append(keys)

print(" My list  ",mylist)





# Adding set of values
# to a single Key
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Updating existing Key's Value
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)

# Adding Nested Key value to Dictionary
Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print("\nAdding a Nested Key: ")
print(Dict)

print("+++++++++++++++++++++")

for x in Dict:
    print(Dict[x])