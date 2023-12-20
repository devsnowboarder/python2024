def is_Palindrome(s):
   return s == s[::-1]



s= "malayalam"
ans = is_Palindrome(s)

if ans:
    print("Yes")
else:
    print("No")