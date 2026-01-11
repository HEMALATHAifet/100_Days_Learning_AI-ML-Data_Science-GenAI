#write a program to count alphabets,digits,special characters in a given string
str=input("enter a string: ")
alpha=0
digit=0
special=0
for char in str:
  if 'A'<=char<='Z' or 'a'<=char<='z':
    alpha+=1
  elif '0'<=char<='9':
    digit+=1
  else:
    special+=1
print("alphabets: ",alpha)
print("digits: ",digit)
print("special characters: ",special)
