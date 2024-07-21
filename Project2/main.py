from random import randint

computer=randint(1,100)
No_of_guess=0
you=-1
while(you!=computer):
    No_of_guess +=1
    you=int(input("guess the Number: "))
    if(you>computer):
        print("Lower Number Places...!")
    else:
        print("Higher Number Places...!")

print(f'You have guessed the number correctly in {No_of_guess} attempt')
if(No_of_guess>=10):
    print("sorry next time you will be win...")
        

    
