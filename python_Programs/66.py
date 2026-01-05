# Check whether the given number is a armstrong number
num = int(input("Enter a number: "))

# Step 1: Count digits manually
temp = num
count = 0

if temp == 0:
    count = 1
else:
    while temp != 0:
        count += 1
        temp //= 10

# Step 2: Calculate sum of powers
temp = num          # reset temp
sum_of_powers = 0

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** count
    temp //= 10

# Step 3: Check Armstrong
if sum_of_powers == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is NOT an Armstrong Number")
