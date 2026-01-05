# check whether a number is perfect square
num = int(input("Enter a number: "))

i = 0
is_square = False

while i * i <= num:
    if i * i == num:
        is_square = True
        break
    i += 1

if is_square:
    print("Perfect Square")
else:
    print("Not a Perfect Square")
