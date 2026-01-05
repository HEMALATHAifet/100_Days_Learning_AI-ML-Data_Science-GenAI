# Print numbers whose sum of digits is a prime number
# Input number
num = int(input("Enter a number: "))

# Calculate sum of digits
temp = num
sum_digits = 0
while temp > 0:
    sum_digits += temp % 10
    temp //= 10

# Check if sum_digits is prime
if sum_digits < 2:
    print("Sum of digits is not prime")
else:
    is_prime = True
    for i in range(2, sum_digits):
        if sum_digits % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Sum of digits is prime")
    else:
        print("Sum of digits is not prime")
