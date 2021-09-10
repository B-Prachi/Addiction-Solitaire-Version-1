# Import required modules
import random
from random import shuffle


# Define a class to create
# all type of cards
class Cards:
    global suites, values
    suites = ['H', 'D', 'C', 'S']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        pass


# Define a class to categorize each card
class Deck(Cards):
    def __init__(self):
       Cards.__init__(self)
       self.mycardset = []
       for n in suites:
            for c in values:
                self.mycardset.append((c)+n)

# Define a class gto shuffle the deck of cards
class ShuffleCards(Deck):

    # Constructor
    def __init__(self):
        Deck.__init__(self)

    # Method to shuffle cards
    def shuffle(self):
        if len(self.mycardset) < 52:
            print("cannot shuffle the cards")
        else:
            shuffle(self.mycardset)
            return self.mycardset

# Driver Code
# Creating objects
objCards = Cards()
objDeck = Deck()

player1Cards = objDeck.mycardset
# Creating object
objShuffleCards = ShuffleCards()
random.shuffle(objShuffleCards.mycardset)
# print(objShuffleCards.mycardset)

# Creating an input file
input_file = open("input.txt", "w")
for element in objShuffleCards.mycardset:
    if element[0] == "A":
        input_file.write("blank")
    else:
        input_file.write(element)
    input_file.write("\n")
input_file.close()
