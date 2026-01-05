# swap two numbers without using third variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swap
a = a + b
b = a - b
a = a - b

print("After swapping: a =", a, "b =", b)
