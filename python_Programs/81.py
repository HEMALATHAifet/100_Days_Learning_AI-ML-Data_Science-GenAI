#Print the sum of first n multiples of a given number
num = int(input("Enter the number: "))
n = int(input("Enter how many multiples to sum: "))

# Using for loop
sum_multiples = 0
for i in range(1, n + 1):
    sum_multiples += num * i

print("Sum of first", n, "multiples of", num, "is:", sum_multiples)
