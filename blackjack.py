"""
try to import pygame as simple gui if you want to use simplegui by codeskulptor in your pc that
has python pygame features installed.
if you dont have the features , then try to copy this code and run at www.codeskulptor.org
"""

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random

# load card 
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
#card image location
card_images = simplegui.load_image("http://ada.cameron.edu/~rp923448/front/front.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
#card image location
card_back = simplegui.load_image("http://ada.cameron.edu/~rp923448/back/back.png")

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
busted = False

# define globals for cards
SUITS = ('Club',
        'Spade',
        'Heart',
        'Diamond'
        )

RANKS = ('A',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        'T',
        'J',
        'Q',
        'K'
        )

VALUES = {'A':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'T':10,
        'J':10,
        'Q':10,
        'K':10
        }

# Blackjack Board
WIDTH = 550
HEIGHT = 550

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print ("Invalid card: ", suit, rank)

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
        self.hand = []

    def __str__(self):
        h = "Hand contains"
        for card in self.hand:
            h += " " + str(card)

        h[:len(h)-1]
        return h

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        """
        # count aces as 1, if the hand has an ace, then add
          10 to hand value if it doesn't bust
        """
        hand_value = 0
        aces = False

        for card in self.hand:

            hand_value += VALUES[card.get_rank()]
            if(card.get_rank() == 'A'):
                aces = True

        #print "get_value(): ", self.hand, hand_value, aces

        if(aces and hand_value + 10 <= 21):
            hand_value += 10

        return hand_value

    def draw(self, canvas, pos):
        SPACE = 15
        for i in range(len(self.hand)):
            p = [pos[0] + ((CARD_SIZE[0] + SPACE) * i), pos[1]]
            self.hand[i].draw(canvas, p)


# define deck class
class Deck:
    def __init__(self):
        """
        Deck Initializer
        """

        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                c = Card(suit, rank)
                self.deck.append(c)

        self.shuffle()

    def shuffle(self):
        """
        Shuffle the deck
        """
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()

    def __str__(self):
        """
        Returns a string representing the deck
        """
        d = "Deck contains"
        for card in self.deck:
            d += " " + str(card)

        return d


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, score

    if(in_play):
        score -= 1

    deck = Deck()
    player_hand = Hand()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.get_value()

    print ("Player Hand: " + str(player_hand) + ", Score: " + str(player_hand.get_value()))
    print ("Dealer Hand: " + str(dealer_hand) + ", Score: " + str(dealer_hand.get_value()))

    outcome = "Hit or stand?"
    in_play = True
    busted = False

def hit():
    """
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update
    in_play and score
    """
    global player_hand, in_play, outcome, score, deck, busted

    if(in_play):
        player_hand.add_card(deck.deal_card())
        print ("Player's hand: " + str(player_hand) + " | Score = " + str(player_hand.get_value()))

        if(player_hand.get_value() > 21):
            outcome = "You have busted! - New deal?"
            in_play = False
            busted = True
            score -= 1

        if(player_hand.get_value() == 21):
            outcome = "Blackjack! You won! New deal?"
            in_play = False
            busted = False
            score += 1
    else:
        if(busted):
            outcome = "You have busted! - New deal?"
        else:
            outcome = "Play finished! - New deal?"

def stand():
    """
    # if hand is in play, repeatedly hit dealer until his
    hand hasvalue 19 or more
    """
    global outcome, in_play, deck, score

    if(not in_play):
        if(busted):
            outcome = "You have busted! - New deal?"
        else:
            outcome = "Play finished! - New deal?"
    else:
        while(dealer_hand.get_value() < 19):
            dealer_hand.add_card(deck.deal_card())

        print("Dealer's hand: " + str(dealer_hand) + " | Score = " + str(dealer_hand.get_value()))

        if(player_hand.get_value() <= dealer_hand.get_value() and dealer_hand.get_value() <= 21):
            outcome = "Dealer Wins! - New deal?"
            score -= 1
        else:
            outcome = "Player Wins! - New deal?"
            score += 1

        if(dealer_hand.get_value() == 21):
            outcome = "Lost! Dealer Blackjack! - New deal?"
            score -= 1

        #outcome += " - New deal?"
        in_play = False

    # assign a message to outcome, update in_play and score

# draw handler
def draw(canvas):
    """

    """
    canvas.draw_text('Blackjack by Rajesh', ((WIDTH / 3), 20), 30, 'Black')

    pos = [(WIDTH / 8), (HEIGHT / 5)]
    dealer_hand.draw(canvas, pos)

    if(in_play):
        canvas.draw_image(
                          card_back,
                          CARD_BACK_CENTER,
                          CARD_BACK_SIZE,
                          [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                          CARD_BACK_SIZE)
    else:
        canvas.draw_text("Dealers's hand: " + str(dealer_hand.get_value()), [(WIDTH / 8), (HEIGHT / 5) - 10], 15, 'Black')

    canvas.draw_text("Dealers's hand:", [(WIDTH / 8), (HEIGHT / 5) - 10], 15, 'Black')
    canvas.draw_text("Player's hand: " + str(player_hand.get_value()), [(WIDTH / 8), (HEIGHT / 5) * 3 - 10], 15, 'Black')

    player_hand.draw(canvas, [(WIDTH / 8), (HEIGHT / 5) * 3])

    canvas.draw_text(outcome, ((WIDTH / 8), (HEIGHT / 2)), 30, 'Black')
    canvas.draw_text("Score: " + str(score), [(WIDTH / 8), (HEIGHT / 5) * 4.5], 40, 'Black')

# initialization frame
frame = simplegui.create_frame("Blackjack", WIDTH, HEIGHT)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 100)
frame.add_button("Hit",  hit, 100)
frame.add_button("Stand", stand, 100)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
