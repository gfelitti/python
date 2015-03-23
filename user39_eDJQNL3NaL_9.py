# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

num_range = 100
secret_number = 0
numb_guesses = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global numb_guesses
    global num_range
    if num_range == 100:
        numb_guesses = 7
        secret_number = random.randint(0, 100)
        print
        print "New game, range is 0 - 100"
        print
    if num_range == 1000:
        numb_guesses = 10
        secret_number = random.randint(0, 1000)
        print
        print "New game, range is 0 - 1000"
        print


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()
    # remove this when you add your code    
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global numb_guesses
    guess = int(guess)
    print "Your guess was " + str(guess)
    numb_guesses = numb_guesses -1
    if numb_guesses ==0 and guess != secret_number:
        print "Game over!"
        print "The right number was " + str(secret_number)
    else:
        if guess < secret_number:
            print "Higher!"
            print "You have " + str(numb_guesses) + " guesses left!"
            print
        if guess > secret_number:
            print "Lower!"
            print "You have " + str(numb_guesses) + " guesses left!"
            print
        if guess == secret_number:
            print "Bullseye!"
            

    # remove this when you add your code
    pass

    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100]", range100, 200)
f.add_button("Range is [0, 1000]", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
