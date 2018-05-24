"""
Design the data structure for a generic deck of cards.
Explain how you would subclass the data structures to implement blackjack.
"""

class Deck():
    def __init__(self):
        self.cards = []


    def new_deck(self):
        values = [2, 3, 4, 5, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']


    def shuffle(self):
        num_of_cards = len(self.cards)


    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

    def __str__(self):
        return str(self.cards)



class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = str(value)

    def __str__(self):
        return '{0} of {1}'.format(self.value, self.suit)



