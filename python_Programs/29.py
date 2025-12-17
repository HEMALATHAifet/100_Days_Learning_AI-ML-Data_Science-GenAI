#create a simple calculator
num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
choice=input("enter choice: ")
if choice=='+':
  print("sum=",num1+num2)
elif choice=='-':
  print("difference=",num1-num2)
elif choice=='*':
  print("product=",num1*num2)
elif choice=='/':
  print("quotient=",num1/num2)
