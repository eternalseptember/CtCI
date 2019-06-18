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

othello_game.begin_game(True)






