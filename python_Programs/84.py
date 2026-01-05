# Find numbers whose sum of digits is divisible by 7
# Input the limit
n = int(input("Enter n: "))

print("Numbers whose sum of digits is divisible by 7:")

for num in range(1, n+1):
    temp = num
    sum_digits = 0
    
    # Find sum of digits
    while temp > 0:
        sum_digits += temp % 10
        temp //= 10
    
    # Check divisibility by 7
    if sum_digits % 7 == 0:
        print(num, end=' ')
