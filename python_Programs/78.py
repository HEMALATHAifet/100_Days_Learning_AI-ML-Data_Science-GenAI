# Find largest & smallest digit in a number

num = int(input("Enter a number: "))

# Initialize largest and smallest
largest = 0
smallest = 9

# Process each digit
while num > 0:
    digit = num % 10       # Get last digit
    if digit > largest:
        largest = digit
    if digit < smallest:
        smallest = digit
    num = num // 10        # Remove last digit

print("Largest digit is:", largest)
print("Smallest digit is:", smallest)
