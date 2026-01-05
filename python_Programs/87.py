# Count the number of prime digits in a number
# Input number
num = int(input("Enter a number: "))

temp = num
count = 0

while temp > 0:
    digit = temp % 10
    if digit in [2, 3, 5, 7]:  # check if digit is prime
        count += 1
    temp //= 10

print("Number of prime digits in", num, "is:", count)
