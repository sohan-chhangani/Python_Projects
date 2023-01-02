import random

random_num = random.randint(1,100)

user_guess = 0

while user_guess != random_num:
    user_guess = int(input("Your guessed number: "))
    
    if(user_guess < random_num ):
        print("!!Guess higher!!")
    if(user_guess > random_num ):
        print("!!Guess Lower!!")
    if(user_guess == random_num):
        print("You guessed it correct \n Congratulations!!!")
        
    