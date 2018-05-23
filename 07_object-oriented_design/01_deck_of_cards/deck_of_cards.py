"""
Design the data structure for a generic deck of cards.
Explain how you would subclass the data structures to implement blackjack.
"""

class Deck():
    def __init__(self):
        self.cards = []


class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = str(value)



