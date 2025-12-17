#add digits in a number which are in odd position
num=int(input("enter a number: "))
out=0
count=1
while num!=0:
    ld=num%10
    if count%1==0:
        out=out+ld
    count=count+1
    num=num//10
print(out)
