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
        self.min_value = 0  # All aces are 1 point each.
        self.max_value = 0  # One ace is 11 points without busting hand.
        self.winning_hand = False  # Hand equals 21.
        self.bust = False


    def show_first_card(self):
        # To be used by the dealer.
        print(self.hand[0])
        print()


    def show_whole_hand(self):
        # To be used by the dealer.
        for card in self.hand:
            print(card)
        print()


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
        self.max_value = self.min_value  # Presetting this value.

        # Check if hand is bust.
        if self.min_value > 21:
            self.winning_hand = False
            self.bust = True  # Eliminated from the game.
            return

        # Max value when one ace is 11 points without busting hand.
        if self.num_of_aces > 0:
            num_of_ones = self.num_of_aces - 1
            max_value = self.base_total + 11 + num_of_ones

            if max_value <= 21:
                self.max_value = max_value  # One ace is 11 points.

        # Check for winning hand combinations.
        if (self.min_value == 21) or (self.max_value == 21):
            self.winning_hand = True

        else:
            # Just in case someone wants to blow their winning hand.
            self.winning_hand = False


    def __str__(self):
        desc = '\t{0}\n'.format(self.player_name)
        desc += 'Base Total: \t{0}\n'.format(self.base_total)
        desc += '# of Aces: \t\t{0}\n'.format(self.num_of_aces)
        desc += 'Min value: \t\t{0}\n'.format(self.min_value)
        desc += 'Max value: \t\t{0}\n'.format(self.max_value)
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
        self.play_order = []  # Players with valid hands.
        self.players = {}


    def show_blackjack_table(self):
        # Show each player's starting hand.
        for player_name in self.play_order:
            print(self.players[player_name])


    def show_winning_players(self, winning_players):
        for player_name in winning_players:
            print(self.players[player_name])


    def add_player(self, player_name):
        # 1-4 players.
        if player_name in self.players:
            print('{0} is already in the game.'.format(player_name))
            return
        if len(self.play_order) >= 4:
            print('This table is full.')
            return

        self.play_order.append(player_name)
        self.players[player_name] = Hand(player_name)


    def deal_two_cards_to_everyone(self):
        for rounds in range(2):
            # Deal cards to players.
            for player_name in self.play_order:
                new_card = self.deck.deal()
                self.players[player_name].get_card(new_card)

            # Deal card to dealer.
            new_card = self.deck.deal()
            self.dealer.get_card(new_card)


    def check_natural_blackjacks(self):
        # If anyone has a natural blackjack, then the game ends.
        blackjack_winners = []

        for player_name in self.play_order:
            if self.players[player_name].winning_hand:
                blackjack_winners.append(player_name)

        return self.dealer.winning_hand, blackjack_winners


    def hit_or_stand(self):
        # Players' turn.
        acceptable_options = ['s', 'S', 'h', 'H']
        hit = self.play_order[:]
        stand = []
        eliminated = []

        while len(hit) > 0:
            # As long as there are players who want cards...
            # Ask all of those players to hit or stand.
            for player_name in hit:
                player_hand = self.players[player_name]
                choice = ''

                while choice not in acceptable_options:
                    print('{0}...'.format(player_name), end=' ')
                    choice = input('[H]it or [S]tand? ')

                if choice.upper() == 'H':  # Hit
                    # Player gets a new card.
                    new_card = self.deck.deal()
                    player_hand.get_card(new_card)

                    # Print new hand.
                    print(player_hand)

                    # If the player busts, they are eliminated from the game.
                    if player_hand.bust:
                        eliminated.append(player_name)

                elif choice.upper() == 'S':  # Stand
                    print(player_hand)
                    stand.append(player_name)


            # Remove players who chose to keep their hand.
            for player_name in stand:
                hit.remove(player_name)

            # Remove players who got eliminated.
            for player_name in eliminated:
                hit.remove(player_name)
                self.play_order.remove(player_name)

            # Reset the lists.
            stand = []
            eliminated = []


    def dealers_turn(self):
        # Draw until hand is worth 17.
        # Could implement other dealer rules.
        while self.dealer.max_value < 17:
            new_card = self.deck.deal()
            self.dealer.get_card(new_card)
            print(new_card)

        print('\n\n')


    def check_for_winners(self):
        # This function runs when the dealer has not busted, and
        # there are players remaining in the game.
        dealer_hand = self.dealer.max_value  # ???
        tied = []
        winners = []

        # Players with higher value than the dealer wins.
        for player_name in self.play_order:
            player_min = self.players[player_name].min_value
            player_max = self.players[player_name].max_value

            if (dealer_hand < player_min) or (dealer_hand < player_max):
                winners.append(player_name)
            elif (dealer_hand == player_min) or (dealer_hand == player_max):
                tied.append(player_name)

        # If winners is an empty list, then tie or the dealer wins.
        return tied, winners


    def begin_game(self):
        if len(self.play_order) <= 0:
            print("No players in the game")
            return


        # Game begins.
        self.deal_two_cards_to_everyone()
        self.show_blackjack_table()
        print('\tDealer\'s First Card:')
        self.dealer.show_first_card()


        # Check for blackjack winners.
        dealer_wins, winning_players = self.check_natural_blackjacks()

        if dealer_wins or (len(winning_players) > 0):
            # Game ends if anyone has a natural blackjack.
            if (dealer_wins is True) and (len(winning_players) > 0):
                print('**************************')
                print('\tThe game is a tie.')
                print('**************************')

                print('\tDealer has blackjack.')
                self.dealer.show_whole_hand()

                print('\tPlayer(s) with blackjack:')
                self.show_winning_players(winning_players)

            elif dealer_wins:
                print('*****************************')
                print('\tDealer has blackjack.')
                print('*****************************')
                self.dealer.show_whole_hand()

            elif len(winning_players) > 0:
                print('*********************************')
                print('\tPlayer(s) with blackjack:')
                print('*********************************')
                self.show_winning_players(winning_players)
            return

        print('No one has a natural blackjack.\n')


        # Players' turn.
        self.hit_or_stand()

        if len(self.play_order) <= 0:
            # If all players bust, then dealer automatically wins.
            print('*************************************************')
            print('\tAll players have busted. The dealer wins.')
            print('*************************************************')
            return


        # Dealer's turn.
        print('\tDealer\'s hand:')
        self.dealer.show_whole_hand()
        print('\tDealer draws:')
        self.dealers_turn()

        # If dealer busted, then the remaining players win.
        if self.dealer.bust:
            print('*******************************************************')
            print('\tThe dealer busted. The remaining player(s) win.')
            print('*******************************************************')
            self.show_winning_players(self.play_order)
            return


        # The dealer has not busted and there are remaining players.
        tied, winning_players = self.check_for_winners()

        if len(winning_players) <= 0:
            if len(tied) > 0:
                print('**************************')
                print('\tThe game is a tie.')
                print('**************************')
                print('\tDealer\'s hand: ')
                self.dealer.show_whole_hand()

                print('\tTied player(s):')
                self.show_winning_players(tied)

            else:
                print('************************')
                print('\tThe dealer wins.')
                print('************************')
                self.dealer.show_whole_hand()

        else:
            print('**************************')
            print('\tWinning player(s):')
            print('**************************')
            self.show_winning_players(winning_players)






