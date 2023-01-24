# Testing indivdual player actions during the game.
# This file tries to reach an end-game state.
# Same game state as 2b, but organized differently.


from othello import *


othello_game = Othello()

# game setup here
othello_game.board = [[None, 'B', 'B', 'B', 'B', 'B', None, None], 
					  ['W', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], 
					  [None, 'B', 'B', 'B', 'B', 'B', None, None], 
					  [None, 'B', 'B', 'B', 'B', 'B', None, None], 
					  ['W', 'B', 'W', 'W', 'W', 'B', 'W', 'W'],
					  ['W', 'B', 'W', 'W', 'W', 'B', 'W', 'W'], 
					  ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'], 
					  [None, 'B', 'B', 'B', 'B', 'B', None, None]]

# white's turn
othello_game.pieces_played = 52
othello_game.playable_spots = [(3, 6), (3, 7), (7, 6), (7, 7), (3, 0),
							   (7, 0), (2, 6), (0, 6), (2, 0), (0, 0),
							   (0, 7), (2, 7)]
othello_game.active_player = 1

othello_game.begin_game(True)






