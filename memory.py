# implementation of card game - Memory

import simplegui
import random

card_width = 45
cards = range(8) + range(8)
exposed = [False, False, False, False, False, False, False, False, False, 
           False, False, False, False, False, False, False]
flipped_card1 = 0
flipped_card2 = 0
turns = 0

# helper function to initialize globals
def new_game():
    global state, turns
    state = 0
    random.shuffle(cards)  
    turns = 0
    print cards
    exposed = [False, False, False, False, False, False, False, False, False, 
           False, False, False, False, False, False, False]
    

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, revealed_index_numbers, state, turns, flipped_card1, flipped_card2
    card_index = pos[0]/50
    print "clicked card index is " + str(card_index)
    
    if exposed[card_index] == True:
        return            

    else:
        if state == 0:
            exposed[card_index] = True   
            flipped_card2 = card_index
            print "flipped_card2 is " + str(card_index)
            state = 1
            print "state = 1a"
            print " "
            
        elif state == 1:        
            exposed[card_index] = True   
            flipped_card1 = card_index
            print "flipped_card1 is " + str(card_index)
            state = 2
            print "state = 2"
            print " "
        
        
        else:
            #It's here we're in state 2.
            turns += 1            
            
            if cards[flipped_card1] != cards[flipped_card2]:
                exposed[flipped_card1] = False
                exposed[flipped_card2] = False
                state = 1
                print "state = 1b"
                print " "                  
        
            elif cards[flipped_card1]  == cards[flipped_card2]:
                exposed[flipped_card1] = True
                exposed[flipped_card2] = True
           
                state = 1
                print "state = 1c"
                print " "
                
            exposed[card_index] = True   
            flipped_card2 = card_index
            print "flipped_card2 is " + str(flipped_card2)     
                
                   
        
#ignoring previously paired cards        
#state == 0 is no cards flipped
#state == 1 is one card flipped
#state == 2 is two cards flipped
#there's always one card exposed
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed, cards

              
    text_location = [0, 65]  
    label.set_text("Turns = " + str(turns))
    
    for card_index in range(len(cards)):               
        if exposed[card_index]:                         
                canvas.draw_text(str(cards[card_index]), (text_location[0] + 15, text_location[1]), 50, 'Tan')
                text_location[0] += 50         
        else:                       
            canvas.draw_polygon([(text_location[0], 0), (text_location[0], 100),
                                (text_location[0] + 50, 100), (text_location[0] + 50, 0)], 
                                2, 'White', 'Green')                                                                                       
            text_location[0] += 50
       


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
