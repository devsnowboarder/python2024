numbers  = [1,2,3,4,5,6,7,8,9,10]

even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))


square_list = map(lambda x: x**2, numbers)
print(list(square_list))


numbers2 = [-1,0,1,-2,2,0]

print(all(num > 0 for num in numbers2))

print(any(num > 0 for num in numbers2))


