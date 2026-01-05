# check whether a number is power of 2
n = int(input("Enter a number: "))
while n % 2 == 0:
    n = n // 2
if n == 1:
    print("Power of 2")
else:
    print("Not a power of 2")
