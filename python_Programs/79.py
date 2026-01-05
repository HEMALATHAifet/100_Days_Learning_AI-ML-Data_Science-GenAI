# count even and odd digits in a number
num = int(input("Enter a number: "))
even_count = 0
odd_count = 0

while num > 0:
    digit = num % 10        # Get last digit
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    num = num // 10         # Remove last digit

print("Even digits count:", even_count)
print("Odd digits count:", odd_count)
