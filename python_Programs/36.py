#write a python program to find first digit of a number
num=int(input("Enter a number: "))
while num>=10:
    num=num//10
print(num)
