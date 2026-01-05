# Check whether a number is a perfect number
num = int(input("Enter a number: "))

if num <= 0:
    print("Not a perfect number")
else:
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i

    if divisor_sum == num:
        print(num, "is a Perfect Number")
    else:
        print(num, "is NOT a Perfect Number")
