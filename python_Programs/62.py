# print all factors a number (- Every factor is a divisor, and every divisor is a factor)
num = int(input("Enter a number: "))

print("Factors of", num, "are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
