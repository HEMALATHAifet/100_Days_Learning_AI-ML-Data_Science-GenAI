#print product of digits
num=int(input("enter a number: "))
out=1
while num!=0:
    ld=num%10
    out=out*ld
    num=num//10
print(out)
