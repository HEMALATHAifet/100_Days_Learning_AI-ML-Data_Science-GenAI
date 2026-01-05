#Reverse digits and add
# Input number
num = int(input("Enter a number: "))

# Reverse the number
rev = 0
temp = num
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

# Add original and reversed number
result = num + rev
print("Result after reversing and adding:", result)
