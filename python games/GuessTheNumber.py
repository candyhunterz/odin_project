import math
import random
import simplegui

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console



# initialize global variables used in your code
secret_num = 0
life = 0
flag = True 

# helper function to start and restart the game
def new_game():
    range100()
    
    
   
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global life, flag, secret_num
    life = 7
    secret_num = random.randrange(0,100)
    print "New game, range is 0-100, 7 guesses left"
    print "take a guess"
    flag
    
    


def range1000():
    # button that changes range to range [0,1000) and restarts
    global secret_num, life, flag
    life = 10
    secret_num = random.randrange(0,1000)
    print "New game, range is 0-1000, 10 guesses left"
    print "take a guess"
    flag = False
   
    
def input_guess(guess):
    # main game logic goes here	
    global life, num_guess
    print "your guess:", guess
    num_guess = int(guess)
    if life == 0:
        print "you lose!"
        print "the number was:" , secret_num
        if flag:
            new_game()
        else:
            range1000()
    elif num_guess < secret_num:
        life -= 1
        print "too low,guesses left:", life
    elif num_guess > secret_num:
        life -= 1
        print "too high, guesses left:", life
    else:
        life -= 1
        print "correct"
        if flag:
            new_game()
        else:
            range1000()
        
# create frame


frame = simplegui.create_frame("Game", 300, 200)
inp = frame.add_input("guess a number", input_guess, 50)

range1 = frame.add_button("0-100", range100, 70)
range2 = frame.add_button("0-1000", range1000, 70)





# register event handlers for control elements

    



# call new_game and start frame
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
