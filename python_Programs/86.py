# Print the reverse of a number without converting to string
# Input number
num = int(input("Enter a number: "))

rev = 0
temp = num

while temp > 0:
    rev = rev * 10 + temp % 10  # add last digit
    temp //= 10                  # remove last digit

print("Reverse of", num, "is:", rev)
