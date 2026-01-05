# Print all palindrome numbers between two numbers
# Input range
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

print("Palindrome numbers between", start, "and", end, ":")

for num in range(start, end + 1):
    temp = num
    rev = 0
    # Reverse the number
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10
    # Check palindrome
    if num == rev:
        print(num, end=' ')
