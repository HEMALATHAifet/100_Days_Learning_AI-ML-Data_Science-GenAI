#write a python program to check greatest among the given 3 numbers
num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
num3=int(input("enter num3: "))
if num1>num2 and num2>num3:
  print("num1 is greater")
elif num2>num1 and num2>num3:
  print("num2 is greater")
else:
  print("num3 is greater")
  
