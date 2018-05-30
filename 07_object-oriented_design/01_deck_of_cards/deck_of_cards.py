"""
Design the data structure for a generic deck of cards.
Explain how you would subclass the data structures to implement blackjack.
"""

"""
Blackjack rules implemented:
Maximum of four players.
All players are dealt two face up cards.
Dealer gets one card faced up and one card faced down.

The game ends if any players or dealer has a natural blackjack.

Players have two options: hit or stand.
Players who busted are eliminated from the game.
If all players busted, then the dealer wins.

Then the dealer reveals the hidden card and draws until it hits 17.
If the dealer busts, then all remaining players win.
Else, the remaining players with a higher total than the dealer wins.
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
        self.base_total = 0  # Without aces.
        self.num_of_aces = 0  # Same as if all aces equal 1.
        self.blackjack = False  # Natural.
        self.min_value = 0  # All aces are 1 point each.
        self.max_value = 0  # One ace is 11 points without busting hand.
        self.winning_hand = False  # Hand equals 21.
        self.bust = False


    def show_first_card(self):
        print('{0}\n'.format(str(self.hand[0])))


    def show_whole_hand(self):
        for card in self.hand:
            print('{0}'.format(str(card)))


    def get_card(self, card):
        self.hand.append(card)

        # Update card type values.
        if type(card.value) is int:
            self.base_total += card.value
        else:
            self.num_of_aces += 1

        # Check for win/lose hands.
        self.calculate_hand()


    def calculate_hand(self):
        # Min value when (No aces) OR (All aces are 1 point each).
        self.min_value = self.base_total + self.num_of_aces
        self.max_value = self.min_value  # Presetting this value

        # Check if hand is bust.
        if self.min_value > 21:
            self.bust = True  # Eliminated from the game.
            return

        # Max value when one ace is 11 points without busting hand.
        if self.num_of_aces > 0:
            num_of_ones = self.num_of_aces - 1
            max_value = self.base_total + 11 + num_of_ones

            if max_value <= 21:
                self.max_value = max_value  # One ace is 11 points.

        # Check for natural blackjack.
        if (len(self.hand) == 2) and (self.max_value == 21):
            self.blackjack = True
            self.winning_hand = True
            return

        # Check for other winning hand combinations.
        if (self.min_value == 21) or (self.max_value == 21):
            self.winning_hand = True
            return


    def __str__(self):
        desc = '\t{0}\n'.format(self.player_name)
        desc += 'Base Total: \t{0}\n'.format(self.base_total)
        desc += '# of Aces: \t\t{0}\n'.format(self.num_of_aces)
        desc += 'Min value: \t\t{0}\n'.format(self.min_value)
        desc += 'Max value: \t\t{0}\n'.format(self.max_value)
        desc += 'Blackjack: \t\t{0}\n'.format(self.blackjack)
        desc += 'Winning hand: \t{0}\n'.format(self.winning_hand)
        desc += 'Bust: \t\t\t{0}\n'.format(self.bust)

        desc += 'Hand:\n'
        if len(self.hand) == 0:
            desc += '\t\tEmpty\n'
        else:
            for card in self.hand:
                desc += '\t\t{0}\n'.format(card)

        return desc


class Blackjack():
    def __init__(self):
        # Deck setup
        self.deck = Deck()
        self.deck.shuffle()

        # Dealer setup
        self.dealer = Hand('Dealer')

        # Board setup
        self.play_order = []
        self.players = {}


    def add_player(self, player_name):
        # 1-4 players.
        if player_name in self.players:
            print('{0} is already in the game.'.format(player_name))
        elif len(self.play_order) == 4:
            print('This table is full.')
        else:
            self.play_order.append(player_name)
            self.players[player_name] = Hand(player_name)


    def deal_two_cards_to_everyone(self):
        for rounds in range(2):
            # Deal cards to players.
            for player in self.play_order:
                new_card = self.deck.deal()
                self.players[player].get_card(new_card)

            # Deal card to dealer.
            new_card = self.deck.deal()
            self.dealer.get_card(new_card)


    def print_blackjack_table(self):
        # Show each player's hand.
        for player in self.play_order:
            print(self.players[player])

        # Show only the first card of the dealer's hand.
        print('\tDealer\'s First Card:')
        self.dealer.show_first_card()


    def check_natural_blackjacks(self):
        # If anyone has a natural blackjack, then the game ends.
        dealer_blackjack = self.dealer.blackjack
        player_blackjack = []

        for player in self.play_order:
            if self.players[player].blackjack:
                player_blackjack.append(player)

        return dealer_blackjack, player_blackjack


    def print_blackjack_round_winners(self, dealer_win, winning_players):
        if (dealer_win is False) and (len(winning_players) == 0):
            print('\tNo one has a natural blackjack.')
            return

        if (dealer_win is False) and (len(winning_players) > 0):
            print('\tWinning player(s):')
            for player in winning_players:
                print('\t{0}:'.format(player))
                winning_hand = self.players[player]
                winning_hand.show_whole_hand()
            return

        if (dealer_win is True) and (len(winning_players) == 0):
            print('\tDealer has blackjack.')
            self.dealer.show_whole_hand()
            return

        if (dealer_win is True) and (len(winning_players) > 0):
            print('\tThe game is a tie.')
            print('\tDealer has blackjack:')
            self.dealer.show_whole_hand()
            print('\tWinning player(s):')
            for player in winning_players:
                print('\t{0}:'.format(player))
                winning_hand = self.players[player]
                winning_hand.show_whole_hand()
            return


    def hit_or_stand(self):
        # Ask each player hit or stand.
        # If the player busts, they are removed from the game.
        # if player.bust:
        # self.play_order.remove(player_name)

        return None


    def dealers_turn(self):
        # Reveals hidden card.
        # Draw until hand is worth 17.

        return None


    def check_for_winners(self):
        # If dealer busted, then remaining players win.
        # Else, players with higher value than the dealer wins.
        winners = []

        # stuff here


        if len(winners) > 0:
            return winners
        else:
            # Tie or dealer wins.
            return None


    def begin_game(self):
        if len(self.play_order) <= 0:
            print("No players in the game")
            return

        self.deal_two_cards_to_everyone()
        self.print_blackjack_table()

        # Game ends if someone has a natural blackjack.
        dealer_wins, winning_players = self.check_natural_blackjacks()
        self.print_blackjack_round_winners(dealer_wins, winning_players)

        """
        # If all players bust, then dealer automatically wins.
        self.hit_or_stand()


        self.dealers_turn()
        self.check_for_winners()
        """





