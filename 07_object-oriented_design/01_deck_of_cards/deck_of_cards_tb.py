from deck_of_cards import *


deck_1 = Deck()
deck_1.shuffle()
print(deck_1)

print('\n\n\n\n')

card_1 = deck_1.deal()
print(card_1)
card_1 = deck_1.deal()
print(card_1)
card_1 = deck_1.deal()
print(card_1)

print('\n\n\n\n')
print(len(deck_1))


