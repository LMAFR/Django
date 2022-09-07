#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

# from cgitb import handler
from random import shuffle
import itertools
import numpy as np

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

deck = list(itertools.product(SUITE, RANKS))

num_RANKS = '2 3 4 5 6 7 8 9 10 11 12 13 14'.split()
val_by_rank = dict(zip(RANKS, num_RANKS))

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self, deck):
        self.deck = deck

    def shuffle_deck(self):
        shuffle(self.deck)
    
    def cut_deck(self):
        size = len(self.deck)
        return self.deck[:int(size/2)], self.deck[int(size/2):]

# Checkpoint for Deck class
# mydeck = Deck(deck)
# print(mydeck.deck)
# mydeck.shuffle_deck()
# print(mydeck.deck)
# player1_deck, player2_deck = mydeck.cut_deck()
# print(player1_deck, player2_deck, "\n", sep="\n")

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, hand = []):
        self.hand = hand

    def __str__(self):
        return "Contains {} cards.".format(len(self.hand))

    def draw_card(self, deck):
        drawn_card = deck.pop()
        self.hand.append(drawn_card)

    def remove_card(self, removed_card):
        self.hand.remove(removed_card)

# Checkpoint for Hand class
# player1_hand = Hand()
# player2_hand = Hand()
# player1_hand.draw_card(player1_deck)
# player1_hand.draw_card(player1_deck)
# player1_hand.draw_card(player1_deck)
# print(player1_hand.hand, player1_deck, "\n", sep="\n")
# player1_hand.remove_card(player1_hand.hand[0])
# player1_hand.remove_card(player1_hand.hand[0])
# print(player1_hand.hand, "\n", sep="\n")

class Player(Hand):
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """
    def __init__(self, name, deck, hand):
        Hand.__init__(self, hand)
        self.name = name
        self.deck = deck
        self.hand = hand

    def check_n_cards(self):
        print("You have {} card(s) in your hand.".format(len(self.hand)))

    def play(self):
        played_card = self.hand[0]
        self.remove_card(played_card)
        return played_card

# Checkpoint for Player class
# player1 = Player("Alejandro", player1_deck, player1_hand.hand)
# player2 = Player("Computer", player2_deck, player2_hand.hand)
# player1.check_n_cards() 
# first_play = player1.play()
# second_play = player1.play()
# print("Your first card played has been {}.".format(first_play), "Your second card played has been {}.".format(second_play), player1.hand, "\n", sep="\n")

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!

# Take the deck
mydeck = Deck(deck)
# Shuffle it
mydeck.shuffle_deck()
# Cut it and give 1 half to each player
player1_deck, player2_deck = mydeck.cut_deck()
print(player1_deck, player2_deck, "\n", sep="\n")

# Create a hand for each player
player1_hand = Hand()
player2_hand = Hand()

# Define the players and their hand and deck
player1 = Player("Alejandro", player1_deck, player1_hand.hand)
player2 = Player("Computer", player2_deck, player2_hand.hand)

player1_points = 0
player2_points = 0

i = 0
n_wars = 1
turn = 0

def play_turn(v1, v2, player_1 = player1, player_2 = player2, deck_1 = player1_deck, deck_2 = player2_deck, dictionary = val_by_rank):
    # Draw
    player_1.draw_card(deck_1)
    player_2.draw_card(deck_2)

    card_1 = player_1.play()
    card_2 = player_2.play()

    v1 += int(dictionary[card_1[1]])
    v2 += int(dictionary[card_2[1]])

    return v1, v2

def war(v1, v2, turn, n = n_wars, points_1 = player1_points, points_2 = player2_points):

    print("Both cards have the same value! This is War!\n")

    val_1, val_2 = play_turn(v1, v2)
    val_1, val_2 = play_turn(val_1, val_2)

    # print(points_1, points_2, n)
    print("Sum of values after draw 2 more: {} {}".format(val_1, val_2))

    if val_1 > val_2:
        points_1 += (2+4*n)
        n = 1
        return turn, points_1, points_2
    elif val_1 < val_2:
        points_2 += (2+4*n)
        n = 1
        return turn, points_1, points_2
    elif val_1 == val_2:
        print("Both cards have the same value! This is War!.\n")
        n += 1
        war(val_1, val_2, turn, n, points_1, points_2)

while len(player1_deck) > 0:
    
    turn += 1

    val_1 = 0
    val_2 = 0

    val_1, val_2 = play_turn(v1 = val_1, v2 = val_2)

    print(val_1, val_2)

    if val_1 > val_2:
        player1_points += 2
        print("Turn {}. Player 1: {} points. Player2: {} points.\n".format(turn, player1_points, player2_points))
    elif val_1 < val_2:
        player2_points += 2
        print("Turn {}. Player 1: {} points. Player2: {} points.\n".format(turn, player1_points, player2_points))
    elif val_1 == val_2:

        if len(player1_deck) < 2:
            print("There are not enough cards in the deck to do War, so in this case each player take its own card (1 point for each of you).")
            player1_points += 1
            player2_points += 1
            print("Turn {}. Player 1: {} points. Player2: {} points.\n".format(turn, player1_points, player2_points))
        else:
            turn, player1_points, player2_points = war(val_1, val_2, turn, n_wars, player1_points, player2_points)
            print("Turn {}. Player 1: {} points. Player2: {} points.\n".format(turn, player1_points, player2_points))

if len(player1_deck) == 0 and len(player2_deck) == 0 and len(player1.hand) == 0 and len(player2.hand) == 0:
    if player1_points > player2_points:
        print("Result: {} has won this game!".format(player1.name))
    elif player1_points < player2_points:
        print("Result: {} has won this game!".format(player2.name))
    else:
        print("Result: Draw!")
