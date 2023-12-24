test_list1 = [5, 4, 1, 3, 2]
test_list2 = [1, 2]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# using list comprehension and index() + len()
# Matching elements count
i=0;
count=0;

#test_list1.index(i) for i in test_list2])
for i in test_list1:
    if test_list1.index(i) in test_list2:
        print(test_list1.index(i))
        count=count+1

print(count)

res = len([test_list1.index(i) for i in test_list2])

# print result
print("The Match indices list count is : " + str(res))