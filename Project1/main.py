import random
'''
1 =snake
0 =water
-1 =gun
'''
computer=random.choice([1,0,-1])
youstr=input("Enter your choice: ")
youdict={"s":1,"w":0,"g":-1}
reverseDict={1:"snake",0:"water",-1:"gun"}
you=youdict[youstr]
print(f"you choosed: {reverseDict[you]}\ncomputer choosed: {reverseDict[computer]}")

if(computer==you):
    print("you are in draw position")
else:
    if(computer==1 and you==0):
        print("you are lose")
    elif(computer==1 and you==-1):
        print("you are win")
    elif(computer==0 and you==1):
        print("you are win")
    elif(computer==0 and you==-1):
        print("you are lose")
    elif(computer==-1 and you==0):
        print("you are win")
    elif(computer==-1 and you==1):
        print("you are lose")
    else:
        print("somthing went to wrong !!!")
print("Game Over :)")
