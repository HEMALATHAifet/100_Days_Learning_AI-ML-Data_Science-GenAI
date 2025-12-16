#write a python program to check whether the given character is consonant or not

char=input("enter a character: ")
if char not in ('aeiouAEIOU'):
  print(char,"is consonant")
else:
  print(char,"is not consonant")
