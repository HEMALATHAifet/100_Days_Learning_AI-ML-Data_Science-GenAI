# check whether the given phone number is valid or not
# Input phone number as a string
phone = input("Enter phone number: ")

# Check length manually
count = 0
for ch in phone:
    count += 1

# Initialize validity flag
is_valid = True

# Check length
if count != 10:
    is_valid = False
else:
    # Check each character is a digit (0-9)
    for ch in phone:
        if ch < '0' or ch > '9':
            is_valid = False
            break
    # Check first digit is 6, 7, 8, or 9
    if phone[0] < '6' or phone[0] > '9':
        is_valid = False

# Print result
if is_valid:
    print("Valid phone number")
else:
    print("Invalid phone number")
