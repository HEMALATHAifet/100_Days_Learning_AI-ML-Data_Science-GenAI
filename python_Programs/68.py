# Check whether the given number is a strong number
num = int(input("Enter a number: "))

temp = num
sum_of_factorials = 0

while temp > 0:
    digit = temp % 10

    # calculate factorial manually
    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    sum_of_factorials += fact
    temp //= 10

if sum_of_factorials == num:
    print(num, "is a Strong Number")
else:
    print(num, "is NOT a Strong Number")
