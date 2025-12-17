#WAP TO CHECK THE LAST DIGIT OF THE GIVEN NUMBER IS ODD , IF IT IS TRUE , PRINT THE LAST DIGIT OF THE NUMBER ELSE PRINT THE NUMBER AS IT IS
num=int(input("enter number: "))
ld=num%10
if ld%2!=0:
  print(ld)
else:
  print(num)
