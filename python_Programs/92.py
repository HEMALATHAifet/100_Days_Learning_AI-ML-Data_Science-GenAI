# print only special characters in the given string
st=input("enter string: ")
for char in st:
  if not('A'<=char<='Z' or 'a'<=char<='z' or '0'<=char<='9'):
    print(char)
