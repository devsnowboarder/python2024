def Convert(string):
    li = list(string.split(" "))
    return li


# Driver code
str1 = "San Francisco California"
print(Convert(str1))
strList = Convert((str1))

strList2 = list(str1.split(" "))

for  str in strList2:
        print(str[::-1], end =" ")  # Print in one line


for x in strList2:
    print("{}\r", x,"  ",strList2.count(x))


#print("{}\r",mikeSet)
