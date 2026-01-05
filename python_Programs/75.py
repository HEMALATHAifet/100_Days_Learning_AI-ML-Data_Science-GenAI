# print sum of squares of digits in a number
num = int(input("Enter a number: "))

# Initialize sum
sum_squares = 0

# Loop through each digit
while num > 0:
    digit = num % 10          # Get last digit
    sum_squares += digit**2   # Add its square to sum
    num = num // 10           # Remove last digit
print("Sum of squares of digits is:", sum_squares)
