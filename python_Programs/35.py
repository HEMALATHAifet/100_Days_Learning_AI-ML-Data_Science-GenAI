#count number of digits in a number (or) find length of the given number
num=4321
count=0
while num!=0:
    ld=num%10
    num=num//10
    count=count+1
print(count)
