#Add odd digits from the given number
num=int(input("enter a number: "))
out=0
while num!=0:
    ld=num%10
    if ld%2==1:
        out=out+ld
    num=num//10
print(out)
