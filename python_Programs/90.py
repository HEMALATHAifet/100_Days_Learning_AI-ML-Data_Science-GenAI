# Print all even or odd numbers in a given range.
# Input range
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Even numbers from {start} to {end}:")
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end=' ')
        
print("\nOdd numbers from {0} to {1}:".format(start, end))
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end=' ')
