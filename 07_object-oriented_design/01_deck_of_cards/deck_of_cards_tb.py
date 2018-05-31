from deck_of_cards import *


# deck = Deck()
# deck.shuffle()
test_player = Hand('Player 1')

"""
# Test case 0: Four aces.
test_player.get_card(Card('Ace', 'Hearts'))
test_player.get_card(Card('Ace', 'Clubs'))
test_player.get_card(Card('Ace', 'Diamonds'))
test_player.get_card(Card('Ace', 'Spades'))


# Test case 1: Blackjack
test_player.get_card(Card('Ace', 'Hearts'))
test_player.get_card(Card(10, 'Hearts'))


# Test case 2: Winning hand. Aces 1 point each.
test_player.get_card(Card('Ace', 'Diamonds'))
test_player.get_card(Card('Ace', 'Spades'))
test_player.get_card(Card('Jack', 'Hearts'))
test_player.get_card(Card(5, 'Clubs'))
test_player.get_card(Card(4, 'Spades'))


# Test case 3: Winning hand. One ace is 11 points.
test_player.get_card(Card(2, 'Clubs'))
test_player.get_card(Card(8, 'Diamonds'))
test_player.get_card(Card('Ace', 'Spades'))


# Test case 4: Winning hand. No aces.
test_player.get_card(Card(7, 'Hearts'))
test_player.get_card(Card(8, 'Clubs'))
test_player.get_card(Card(6, 'Diamonds'))


# Test case 5: Busted hand. One ace.
test_player.get_card(Card('Ace', 'Diamonds'))
test_player.get_card(Card(9, 'Hearts'))
test_player.get_card(Card('Jack', 'Clubs'))
test_player.get_card(Card(2, 'Diamonds'))
"""

# Test case 6: Not winning hand. Two aces.
test_player.get_card(Card('Ace', 'Diamonds'))
# test_player.get_card(Card('Ace', 'Hearts'))
test_player.get_card(Card('Jack', 'Clubs'))


print(test_player)



