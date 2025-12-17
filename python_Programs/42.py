#WAP TO FIND THE GREATEST AMONG THE 4 NUMBERS
num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
num3=int(input("enter num3: "))
num4=int(input("enter num4: "))
if num1>num2 and num1>num3 and num1>num4:
    print("num1 is greatest number")
elif num2>num1 and num2>num3 and num2>num4:
    print("num2 is greatest number")
elif num3>num1 and num3>num2 and num3>num4:
    print("num3 is greatest number")
else:
  print("num4 is greatest number")
