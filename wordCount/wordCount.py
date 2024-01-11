from collections import Counter

text = open ("/Users/michaellau/python2024/python2024/wordCount/data.txt", 'r')
lines = list(text)
text.close()
wordlist = list()
words_all = 0
for line in lines:
    words_all = words_all + len(line.split())
  #  print(line.split())
   # print(len(line.split()))
    for x in line.split():
        print(x)
        wordlist.append((x))

counter_obj = Counter(wordlist)
print(counter_obj)

for keys, value in counter_obj.items():
    print(" key =  ", keys)
    print(" value =", value)

max =0
for keys, value in counter_obj.items():
       print("Item: ", keys," Frequency: ", value)
       if ( value > max):
           max = value
           maxW = keys


#print('Total words:   ', words_all)

print("maxW ",maxW,"     ",max )
