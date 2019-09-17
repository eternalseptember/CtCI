# Testing the minesweeper game

from minesweeper import *


game = Minesweeper(10, 10)
game.print_board()
# game.choose_cell(4, 4)


# Testing list neighboring cells

# Somewhere in the middle
neigh_cells = game.list_neighboring_cells(4, 4)
print(neigh_cells)

# Corners

