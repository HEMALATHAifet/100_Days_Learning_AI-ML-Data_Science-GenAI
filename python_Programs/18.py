#WAP TO PRINT FIRSTNAME,LASTNAME, IF FIRST CHARACTER IN THE LASTNAME AND LAST CHARACTER IN THE FIRSTNAME ARE DIFFERENT ,ELSE IGNORE
first_name=input("enter first name: ")
last_name=input("enter last name: ")
if   last_name[0]!=first_name[-1]:
  print("first name is ",first_name)
  print("last name is ",last_name)
else:
  print("ignore")
