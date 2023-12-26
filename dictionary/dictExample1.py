per = { 'name' : 'A' ,
        'age' : 20 ,
        'salary' : 500000.00 ,
        'city' : 'Delhi' ,
        'country' : 'IND' }


print(per.keys())
emp_dict = {}
print(emp_dict.keys())

print('\nKey after update \n')
per["weight"] = 70
print(per.keys())




print('\nKey after update \n')
per.update({'body' : 170})
print(per.keys())

