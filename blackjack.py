# Blackjack

import simplegui


# load card sprite - 936x384 - source: jfitz.com


# initialize some useful global variables

score = 0

# define globals for cards


# define card class


# define hand class

        
# define deck class 
        


#define event handlers for buttons


# if busted, assign a message to outcome, update in_play and score
       

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below



# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.set_draw_handler(draw)


# get things rolling

frame.start()


# remember to review the gradic rubric
