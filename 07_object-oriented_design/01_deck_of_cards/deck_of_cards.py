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


class Hand():
    def __init__(self, player_name):
        self.player_name = player_name
        self.hand = []


    def get_card(self, new_card):
        self.hand.append(new_card)


    def __str__(self):
        return '{0}\'s hand: \n\t{1}'.format(self.player_name, self.hand)


class Blackjack_Game():
    def __init__(self):
        self.play_order = []
        self.players = {}
        self.deck = Deck()
        self.deck.shuffle()


    def add_player(self, player_name):
        self.play_order.append(player_name)
        self.players[player_name] = Hand(player_name)


    def deal_cards_to_everyone(self):
        for player in self.play_order:
            if len(self.deck) > 0:
                new_card = self.deck.deal()
                self.players[player].get_card(new_card)


    def check_for_winners(self):
        # aces are 1 or 11
        # anyone with ace and ten/suits wins

        # the players with 21 in their hand wins
        # else the players closest to 21 without going over wins
        # return the list of winners
        return None


    def deal_additional_cards(self):
        # ask which players want an additional card
        want_more_cards = self.play_order[:]

        # if the player does not want another card
        # remove from want_more_cards

        return None


    def begin_game(self):
        if len(self.play_order) <= 0:
            print("No players in the game")
            return

        self.deal_cards_to_everyone()
        self.deal_cards_to_everyone()

        """
        self.check_for_winners()
        self.deal_additional_cards()
        self.check_for_winners()
        """





