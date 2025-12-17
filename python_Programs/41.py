# WAP TO CONSOLIDATE THE STUDENT GRADE FROM 5 SUBJECT MARKS. PRINT 'A' GRADE IF THEIR PERCENTAGE  IS >90 OR PRINT 'B' GRADE IF THEIR PERCENTAGE IS >75 AND <=90 OR PRINT 'C' GRADE IF THEIR PERCENTAGE IS >65 AND <=75 OR PRINT '0' IF THEIR PERCENTAGE IS <=65
sub1=int(input("enter sub1 marks: "))
sub2=int(input("enter sub2 marks: "))
sub3=int(input("enter sub3 marks: "))
sub4=int(input("enter sub4 marks: "))
sub5=int(input("enter sub5 marks: "))
average=(sub1+sub2+sub3+sub4+sub5)/5
print("average of five subjects:",average)
if average>=90:
    print("grade:A")
elif average>=80 and average<90:
    print("grade:B")
elif average>=70 and average<80:
    print("grade:C")
