#WAP TO FIND THE second GREATEST AMONG THE 4 NUMBERS
num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
num3=int(input("enter num3: "))
num4=int(input("enter num4: "))
if num1>num2 and num1>num3 and num1>num4:
    print("num1 is first greatest number")
    if num2>num3 and num2>num4:
        print("num2 is second greatest number")
    elif num3>num4 and num3>num2:
        print("num3 is second greatest number")
    else:
        print("num4 is second greatest number")

if num2>num1 and num2>num3 and num2>num4:
    print("num2 is first greatest number")
    if num1>num3 and num1>num4:
        print("num1 is second greatest number")
    elif num3>num4 and num3>num2:
        print("num3 is second greatest number")
    else:
        print("num4 is second greatest number")
        
if num3>num1 and num3>num2 and num3>num4:
    print("num3 is first greatest number")
    if num1>num2 and num1>num4:
        print("num1 is second greatest number")
    elif num2>num4 and num2>num1:
        print("num2 is second greatest number")
    else:
        print("num4 is second greatest number")

if num4>num1 and num4>num3 and num4>num2:
    print("num4 is first greatest number")
    if num1>num3 and num1>num2:
        print("num1 is second greatest number")
    elif num2>num3 and num3>num1:
        print("num2 is second greatest number")
    else:
        print("num3 is second greatest number")
