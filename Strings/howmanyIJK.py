



seq ="AACCBBXXXX"
count =0;
x = seq[0]


maxNum=0;

for y in range(0,len(seq)):
   # print(seq[y])
    if str(x)== str(seq[y]):
        count=count+1
    else:
        print(str(x)+' '+str(count))
        x = str(seq[y])
        count=1;

print(str(x) + ' ' + str(count))

for x in range(0,len(seq)):
  if ( x == str(x)):
      count = count +1
  else:
      max2 = count

  if max2 > maxNum :
       maxNum = max2


print(maxNum)
