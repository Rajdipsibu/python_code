import random
#function defination..............
def game():
    print("you are Playing the Game...")
    score=random.randint(1,50)#its generate a random no in range 1 to 50
    #fatch the hi-score
    with open("hiscore.txt") as f:
        hiscore=f.read()#give a string value by the read()function
        if(hiscore !=""):
            hiscore=int(hiscore)#covert the string value to integer
        else:
            hiscore=0
    print(f'your score = {score}')
    #main logic required by the question...
    if(score>hiscore):
        with open('hiscore.txt','w') as f:
            f.write(str(score))#string value required in write()function
    return score

#function call.........
game()
