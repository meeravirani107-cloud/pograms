'''student marksheet '''

sub1=int(input("Enter First Sub Marks:="))
sub2=int(input("Enter Second Sub Marks:="))
sub3=int(input("Enter Third Sub Marks:="))

total=sub1+sub2+sub3
per=total/3

if(sub1<40 or sub2<40 or sub3<40): 
   print("Sorry You Are Fail")
else:
  print("The Total Is:=",total)
  print("The Percentage Is:=",per)
  if(per>=80):
    print("The Class Is Distinction")
  elif(per>=60):
    print("The Class Is  First Class")
  elif(per>=40):  
    print("The Class Is  Pass")
  else:
     print("Fail")
