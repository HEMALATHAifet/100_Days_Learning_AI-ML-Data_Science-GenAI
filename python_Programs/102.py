# write a program to add ASCII value of all the special symbols in a given input string
s = input("enter a string: ")
sum=0
for char in s:
    if not (('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('0' <= char <= '9')):
       print(char,"=",ord(char))
       sum=sum+ord(char)
print("sum=",sum)
