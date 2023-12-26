from typing import TextIO

file1: TextIO = open("myfile.txt")

# Reading from file
print(file1.read())
   file1.close()
   file1 = open("myfile.txt", "a")

# Writing to file
    file1.write("\nWriting to file :)")

# Closing file
    file1.close()

f = open("myfile.txt", 'r')

# read()
text = f.read(10)

print(text)
f.close()

f = open("myfile.txt", 'r')

# read()
text = f.read(100)

print(text)
f.close()