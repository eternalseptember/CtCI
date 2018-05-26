"""
Design the data structure for a generic deck of cards.
Explain how you would subclass the data structures to implement blackjack.
"""


class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '{0} of {1}'.format(self.rank, self.suit)


class Deck():
    def __init__(self):
        self.cards = self.new_deck()


    def new_deck(self):
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']

        new_deck = []

        for rank in ranks:
            for suit in suits:
                new_deck.append(Card(rank, suit))

        return new_deck


    def shuffle(self):
        from random import randrange

        num_of_cards = len(self.cards)
        new_deck = []

        while num_of_cards > 0:
            rand_num = randrange(num_of_cards)
            new_deck.append(self.cards.pop(rand_num))
            num_of_cards -= 1

        self.cards = new_deck


    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None


    def __str__(self):
        if len(self.cards) == 0:
            return 'No cards in deck'

        deck_list = ''

        for card in self.cards:
            deck_list += '{0}\n'.format(card)

        return deck_list


class Blackjack_Game():
    def __init__(self):
        deck = Deck()
        deck.shuffle()

    # aces are 1 or 11
    # deal two cards to players
    # anyone with ace and ten/suits wins

    # players decide to draw or not
    # when all players have stopped drawing cards
    # the players with 21 in their hand wins
    # else the players closest to 21 without going over wins





