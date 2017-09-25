# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
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
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
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

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        aces = False
        for card in self.hand:
            card_rank = card.get_rank()
            hand_value += VALUES.get(card_rank)
            if card_rank == 'A':
                aces = True       
          
        if aces == False:
            return hand_value
        if aces == True:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value
    
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.hand:
            card_card.draw(canvas, pos)
            #card_loc = (card_size[0] * (0.5 + RANKS.index(self.rank)), card_size[1] * (0.5 + SUITS.index(self.suit)))
            #canvas.draw_image(card_images, card_loc, card_size, [pos[0] + card_size[0] / 2, pos[1] + card_size[1] / 2], card_size)
            pos[0] = pos[0] + 50
 
        
# define deck class 
        
class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]	# create a Deck object

         

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)   # use random.shuffle()

    def deal_card(self):
            # deal a card object from the deck
        dealt_card = self.deck.pop(0)
        return dealt_card
    
    def __str__(self):
            # return a string representing the deck
        deck_string = ""
        for card in self.deck:
            card = str(card)
            deck_string = deck_string + " " + card
        return "Deck contains " + deck_string



#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand
    deck = Deck()

    player_hand = Hand()
    dealer_hand = Hand()
    deck.shuffle()
    
    card_in_play = deck.deal_card()
    print card_in_play
    player_hand.add_card(card_in_play) 
    card_in_play = deck.deal_card()
    print card_in_play
    player_hand.add_card(card_in_play)   
    print "Player " + str(player_hand)
    
    card_in_play = deck.deal_card()
    print card_in_play
    dealer_hand.add_card(card_in_play) 
    card_in_play = deck.deal_card()
    print card_in_play
    dealer_hand.add_card(card_in_play)
    print "Dealer " + str(dealer_hand)
    
    in_play = True

def hit():
        # if the hand is in play, hit the player
    global score
    if player_hand.get_value() <= 21:
        card_in_play = deck.deal_card()
        print card_in_play
        player_hand.add_card(card_in_play)
        print "Player " + str(player_hand)
        print "Player hand value is " + str(player_hand.get_value())
        outcome = "Hit or stand?"
    else:
        outcome = "You have busted. New deal?"
        print "Player hand value is " + str(player_hand.get_value())
        in_play = False
        score -= 1


    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global score
    player_value = player_hand.get_value()
    print player_value    
    if player_value  > 21:       
        outcome =  "You have busted.  New deal?"
    else: 
        dealer_value = dealer_hand.get_value()
        while dealer_value <= 17:
            card_in_play = deck.deal_card()
            print card_in_play
            dealer_hand.add_card(card_in_play)
            dealer_value = dealer_hand.get_value()
            print "Dealer " + str(dealer_hand)
            print "Dealer value is " + str(dealer_hand.get_value())
        if dealer_value > 21:
            score += 1
            outcome =  "Dealer has busted. You win!  New deal?"
        else:
            if player_value > dealer_value:
                score += 1
                outcome =  "You win!  New deal?"                
            if player_value <= dealer_value:
                score -= 1
                outcome =  "Dealer wins.  New deal?"

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    #card = Card("S", "A")
    player_hand  = Hand()
    player_hand.draw(canvas, [100, 300])
    canvas.draw_text("It's Blackjack!", [210, 100], 36, "black")
    canvas.draw_text(outcome, [150, 200], 25, "black")


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)

frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
