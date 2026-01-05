# check whether the given number is a palindrome
num = int(input("Enter a number: "))

temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if reverse == num:
    print(num, "is a Palindrome Number")
else:
    print(num, "is NOT a Palindrome Number")
