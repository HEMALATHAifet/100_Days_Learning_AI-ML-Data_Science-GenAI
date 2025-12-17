#print sum of digits in a number
num=int(input("enter a number: "))
out=0
while num!=0:
    ld=num%10
    out=out+ld
    num=num//10
print(out)
