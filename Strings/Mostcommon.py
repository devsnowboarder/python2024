from collections import Counter
s = 'lkseropewdssafsdfafkpwe'
print("Original string: "+s)
print("Most common three characters of the said string:")
print(Counter(s).most_common(5))

s2 = s

for x in s2 :
  print(x.count(x))