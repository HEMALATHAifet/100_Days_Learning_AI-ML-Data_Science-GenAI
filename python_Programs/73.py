# check whether a number is perfect cube
n = int(input("Enter a number: "))
i = 0
while i**3 <= n:
    if i**3 == n:
        print(n, "is a perfect cube")
        break
    i += 1
else:
    print(n, "is not a perfect cube.")
