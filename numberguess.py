# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

num_range = 100
num_guesses = 7

# helper function to start and restart the game
def new_game():
    global secret_number
    print "New game. Range is from 0 to " + str(num_range)
    secret_number = random.randrange(0, num_range)
    global num_guesses
    if num_range == 100:
        num_guesses = 7  
    elif num_range == 1000: 
        num_guesses = 10




# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global num_guesses

    num_guesses = 7
    new_game()
    

def range1000():
    
    global num_guesses
    global num_range
    num_guesses = 10
    num_range = 1000
    # button that changes the range to [0,1000) and starts a new game     

    
    new_game()
    return num_range
    
def input_guess(guess):
    # main game logic goes here	
    global num_guesses
    print "Guess was " + guess
    player_guess = int(guess)
    if player_guess == secret_number:
            print "You Win!"
            new_game()
    
    elif num_guesses == 1:        
        print "You ran out of guesses. The number was " + str(secret_number) + "."
        new_game()
    else:         
        num_guesses = num_guesses - 1
        
        if player_guess < secret_number:
            print "Number of remaining guesses is " + str(num_guesses)
            print "Higher!"
        elif player_guess > secret_number:
            print "Number of remaining guesses is " + str(num_guesses)
            print "Lower!"

    
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)

# register event handlers for control elements and start frame

frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter", input_guess, 200)


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric


