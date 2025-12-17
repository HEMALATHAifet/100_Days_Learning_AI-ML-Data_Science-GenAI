#WAP TO PRINT 'ONE DIGIT' IF THE GIVEN NUMBER HAS SINGLE DIGIT OR PRINT 'TEO DIGIT' IF THE GIVEN NUMBER HAS DOUBLE DIGIT OR PRINT 'THREE DIGIT' IF THE GIVEN NUMBER HAS TRIPLE DIGIT ELSE PRINT THE NUMBER AS IT IS IF THE NUMBER HAS MORE THAN THREE DIGIT
num=int(input("enter a number: "))
count=0
while num!=0:
  ld=num%10
  num=num//10
  count=count+1
if count==1:
  print("it is one digit")
elif count==2:
  print("it is two digit")
elif count==3:
  print("it is three digit")
else:
  print("it has more than three digit")
