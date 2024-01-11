listA =['title', 'email', 'password2', 'password1', 'first_name', 'last_name', 'next', 'newsletter']


a, b = listA.index('password2'), listA.index('password1')
listA[b], listA[a]  = listA[a], listA[b]
print(listA)



for i in range(len(listA)):
    try:
      listA[i+1]
    except IndexError:
      continue
    else:
      listA[i],listA[i+1] = listA[i+1],listA[i]


print(listA)




arr = [1, 2, 3, 4, 5]
print(arr)
arr[arr[0]] , arr[0] = arr[0] , arr[arr[0]]
print(arr)

prime_numbers = [2, 3, 5, 7]

# reverse the order of list elements
prime_numbers.reverse()


print('Reversed List:', prime_numbers)

count = prime_numbers.count(2)
print(count)
