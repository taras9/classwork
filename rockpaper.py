# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == "rock":
        name = 0
    elif  name == "Spock":
        name = 1
    elif  name == "paper":
        name = 2
    elif  name == "lizard":
        name = 3
    elif  name == "scissors":
        name =  4     
    else:
        name =  "bad name"
    return name

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        name = "rock"
    elif  number == 1:
        name = "Spock"
    elif  number == 2:
        name = "paper"
    elif  number == 3:
        name = "lizard"
    elif  number == 4:
        name = "scissors"     
    else:
        number = "bad number"
    return name
    
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
 
    
    # print a blank line to separate consecutive games
    print ""

    # print out the message for the player's choice
    
    print "Player chooses " + player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)    

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 4)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses " + str(comp_choice)

    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number) % 5
    

    

    # use if/elif/else to determine winner, print winner message
    if comp_number == player_number:
        print "Player and computer tie!"
    elif difference == 1 or 2:
        print "Player wins!"
    elif difference == 3 or 4:
        print "Computer wins!"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


