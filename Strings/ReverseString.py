

mytxt = "I wonder how this text looks like backwards"
print(mytxt)

print(mytxt.split(" "))

reverse2 = " "
for x in mytxt.split(" "):
    print(x[::-1])
    k = x[::-1]
    reverse2 = " "+ k + reverse2


print(reverse2.split(" "))

revlist = list()

for y in reverse2.split(" "):
    print(y)
    revlist.append(y)


print(revlist[::-1])

revText =" "
for x in revlist:
    print(x)
    revText = " " + x + revText
    print(revText)





