test_str = "GeeksforGeeks"

# using naive method to get count
# of each element in string
all_freq = {}

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

# printing result
print("Count of all characters in GeeksforGeeks is :\n "
      + str(all_freq))

from collections import Counter

# initializing string
test_str = "GeeksforGeeks"

# using collections.Counter() to get
# count of each element in string
res = Counter(test_str)

# printing result
print("Count of all characters in GeeksforGeeks is :\n "
      + str(res))

test_str = "GGGeeksforGeeksabababaaaaaaaa"

# using dict.get() to get count
# of each element in string
res = {}

for keys in test_str:
    res[keys] = res.get(keys, 0) + 1

# printing result


if ( res['G']> 1):
 print(res['G'])

a=set()
max2 =0
for x in test_str:
    if ( res[x] > max2):
         max2 = res[x]


print("Count of all characters in GeeksforGeeks is : \n" + str(res))
res = Counter(test_str)
res = max(res, key=res.get)


print("The maximum of all characters in GeeksforGeeks is :" + str(res) +"  "+ str(max2))
print(a)




test_str2 = "sample program"
res2 = Counter(test_str2)
res2 = max(res, key=res2.get)
print("Maximum occurring character =" +str(res2))