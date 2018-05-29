"""
Design the data structure for a generic deck of cards.
Explain how you would subclass the data structures to implement blackjack.
"""

"""
Blackjack rules implemented:
All players are dealt face up cards.
Dealer gets one card faced up and one card faced down.
"""


class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

        if type(rank) is int:
            self.value = rank
        elif rank is not 'Ace':
            self.value = 10
        else:
            self.value = 'Ace'

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
            return self.cards.pop(0)
        else:
            return None


    def __len__(self):
        return len(self.cards)


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
        self.totals = 0


    def get_card(self, new_card):
        self.hand.append(new_card)


    def calculate_values(self):
        num_of_aces = 0
        base_total = 0

        for card in self.hand:
            if type(card.value) is int:
                base_total += card.value
            else:
                num_of_aces += 1



    def __str__(self):
        if len(self.hand) == 0:
            in_hand = 'Empty'
        else:
            in_hand = ''

            for card in self.hand:
                in_hand += '{0}\n'.format(card)

        return '\t\t{0}\'s hand: \n{1}'.format(self.player_name, in_hand)


class Blackjack_Game():
    def __init__(self):
        self.play_order = []
        self.players = {}
        self.deck = Deck()
        self.deck.shuffle()


    def add_player(self, player_name):
        if player_name in self.players:
            print('{0} is already in the game.'.format(player_name))
        else:
            self.play_order.append(player_name)
            self.players[player_name] = Hand(player_name)


    def deal_cards_to_everyone(self):
        for player in self.play_order:
            if len(self.deck) > 0:
                new_card = self.deck.deal()
                self.players[player].get_card(new_card)


    def check_dealer_blackjack(self):
        # if the dealer has blackjack, then
        # the game ends if no other players have blackjack.

        return None


    def deal_additional_cards(self):
        # ask which players want an additional card
        want_more_cards = self.play_order[:]

        # if the player does not want another card
        # remove from want_more_cards

        return None


    def check_for_winners(self):
        winners = []
        # higher than dealer without bust


        if len(winners) > 0:
            return winners
        else:
            # All players have busted their hands.
            return None


    def begin_game(self):
        if len(self.play_order) <= 0:
            print("No players in the game")
            return

        self.deal_cards_to_everyone()
        self.deal_cards_to_everyone()
        self.check_dealer_blackjack()
        self.deal_additional_cards()
        self.check_for_winners()






