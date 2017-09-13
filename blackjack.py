# Blackjack

import simplegui


# load card sprite - 936x384 - source: jfitz.com
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png") 
CARD_SIZE = (72, 96)

# initialize some useful global variables

score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            print "Invalid card."

    def __str__(self):
        return self.suit + self.rank

        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []	# create Hand object

    def __str__(self):
        # return a string representation of a hand
        what_is_in_hand = ""
        for c in self.hand:
            what_is_in_hand = what_is_in_hand + " " + str(c)           
        return "Hand contains " + what_is_in_hand

    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        
    def __str__(self):
        # return a string representing the deck
        deck_string = ""
        for card in self.deck:
            card = str(card)
            deck_string = deck_string + " " + card
        return "Deck contains " + deck_string
    
print Deck()  
    
#define event handlers for buttons


# if busted, assign a message to outcome, update in_play and score
       

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
#def draw(canvas):
    # test to make sure that card.draw works, replace with your code below



# initialization frame
#frame = simplegui.create_frame("Blackjack", 600, 600)
#frame.set_canvas_background("Green")

#create buttons and canvas callback
#frame.add_button("Deal", deal, 200)
#frame.set_draw_handler(draw)


# get things rolling

#frame.start()


# remember to review the gradic rubric
