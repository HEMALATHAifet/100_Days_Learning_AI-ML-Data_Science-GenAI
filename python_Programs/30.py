#WAP TO CHECK WHETHER THE GIVEN 4 VALUES REPRESENT EITHER SQUARE OR RECTANGLE OR NOT . ELSE PRINT INVALID SHAPE ANGLE
side1=int(input("enter side1: "))
side2=int(input("enter side2: "))
side3=int(input("enter side3: "))
side4=int(input("enter side4: "))
if side1==side2==side3==side4:
  print("it is a square")
elif side1==side3 and side2==side4:
  print("it is a rectangle")
else:
  print("it is a invalid shape"
