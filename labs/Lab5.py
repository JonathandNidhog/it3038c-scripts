import random

GameStatus = 1
randomNum = random.randint(0,100)


print("This is a game guess game")
print("start guess your number")
print("please input your answer")
while (GameStatus == 1):
   
    Gnumber = int(input())
    if Gnumber < randomNum :
        print("your number is small, please try again")
    elif Gnumber > randomNum :
        print('your number is too big please try again')
    elif Gnumber == randomNum :
        print(" your number is correct")
        print("would your want to take another round?(Y/N)")
        Continue = input()
        if Continue == 'Y':
            GameStatus = 1
        if Continue == 'y':
            GameStatus = 1
        if Continue == 'N' :
            GameStatus = 0
            print("game FINISHED")
        if Continue == 'n' :
            GameStatus = 0
            print("game FINISHED")
        

    


