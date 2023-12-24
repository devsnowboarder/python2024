

str1 ="aabbaa"

for x in str1:
    print(x)


reversedString=[]
index = len(str1) # calculate length of string and save in index
while index > 0:
    reversedString += str1[ index - 1 ] # save the value of str[index-1] in reverseString
    index = index - 1 # decrement index
print(reversedString) # reversed string



reversedstring=''.join(reversed(str1))
print(reversedstring)
print(str1)

if  str(reversedString.__eq__(str1)):
    print(" Is Palindome")
else:
    print(" Is NOT Palindome")