import random

random=random.choice(range(1,100))
count=0
guess=input("please enter a number from 1 to 100")
guess=int(guess)

while (True):

    count+=1
    if guess==random :
         print("You Won")
         print("You have tried",count,"times")
         break
    if guess > random :
        print("You Are Close")
        guess=input("enter a smaller one")
        guess=int(guess)
        if guess > random :
            guess = input("enter a SMALLER one!!!, are you idiot???")
            guess = int(guess)
    if guess < random:
        print("You Are Close")
        guess = input("enter a bigger one")
        guess = int(guess)
        if guess < random :
            guess = input("enter a BIGGER one!!!, are you out of your mind???")
            guess = int(guess)



