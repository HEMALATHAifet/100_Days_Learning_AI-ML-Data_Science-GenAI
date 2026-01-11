#print characters which are not vowels
str=input("enter a string: ")
for char in str:
  if 'A'<=char<='Z' or 'a'<=char<='z':
    if char not in 'AEIOUaeiou':
      print(char)
