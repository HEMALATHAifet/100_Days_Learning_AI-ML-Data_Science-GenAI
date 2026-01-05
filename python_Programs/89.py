# Find the digital root of a number
num = int(input("Enter a number: "))

# Repeat until number is a single digit
while num >= 10:
    temp = num
    sum_digits = 0
    while temp > 0:
        sum_digits += temp % 10
        temp //= 10
    num = sum_digits

print("Digital root is:", num)
