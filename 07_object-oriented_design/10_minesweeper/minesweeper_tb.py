# Testing the minesweeper game

from minesweeper import *


game = Minesweeper(10, 10)
game.import_board()
# game.print_board(True)
game.choose_cell(7, 5, 'F')  # invalid cell
game.choose_cell(5, 6, 'F')  # flagging
game.choose_cell(5, 6, 'U')  # un-flagging
game.choose_cell(5, 6, 'F')  # re-flagging
game.choose_cell(4, 6)  # not a mine
game.choose_cell(3, 7)  # should be blanks
# game.choose_cell(5, 2)  # mine

# continuing with the game to check endgame conditions
game.choose_cell(6, 7)
game.choose_cell(6, 8)
game.choose_cell(7, 7, 'F')
game.choose_cell(7, 8)
game.choose_cell(6, 9, 'F')
game.choose_cell(7, 9, 'F')
game.choose_cell(2, 5, 'F')
game.choose_cell(2, 4)
game.choose_cell(2, 3)
game.choose_cell(5, 2, 'F')
game.choose_cell(6, 0, 'F')
game.choose_cell(5, 1)
game.choose_cell(5, 0)
game.choose_cell(4, 0)
game.choose_cell(4, 2)
game.choose_cell(3, 2, 'F')







"""
# Testing functions
game.print_board()
game.choose_cell(4, 4)  # first cell to set the game
print('initial', end=' ')
game.print_score()
print('mine locations of generated board:\n\t', end='')
game.print_mine_loc()
print('... exporting board ...')
game.export_board()
print('... importing board ...')
game.import_board()
print('imported', end=' ')
game.print_score()
print('mine locations of imported board:\n\t', end='')
game.print_mine_loc()
"""


"""
def print_neigh_cells(game, row, col):
    neigh_cells = game.list_neighboring_cells(row, col)
    print(neigh_cells)


# Testing list neighboring cells
# Somewhere in the middle
print_neigh_cells(game, 4, 4)

# Corners - clockwise
print_neigh_cells(game, 0, 0)  # NW
print_neigh_cells(game, 0, 9)  # NE
print_neigh_cells(game, 9, 9)  # SE
print_neigh_cells(game, 9, 0)  # SW
"""



