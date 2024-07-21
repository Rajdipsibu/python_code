sub1=int(input("enter the marks of sub1: "))
sub2=int(input("enter the marks of sub2: "))
sub3=int(input("enter the marks of sub3: "))
total_Percentage=(100*(sub1+sub2+sub3))/300

if(total_Percentage >= 40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("you are pass")
# elif(sub1>=33 and sub2>=33 and sub3>=33):
#     print("you are almost pass")
else:
    print("batter luck next time..!",total_Percentage)