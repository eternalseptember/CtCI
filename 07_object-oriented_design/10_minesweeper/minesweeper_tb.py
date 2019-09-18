# Testing the minesweeper game

from minesweeper import *


def print_neigh_cells(game, row, col):
    neigh_cells = game.list_neighboring_cells(row, col)
    print(neigh_cells)


game = Minesweeper(10, 10)
game.print_board()
game.choose_cell(4, 4)


# Testing list neighboring cells

# Somewhere in the middle
print_neigh_cells(game, 4, 4)

# Corners - clockwise
print_neigh_cells(game, 0, 0)  # NW
print_neigh_cells(game, 0, 9)  # NE
print_neigh_cells(game, 9, 9)  # SE
print_neigh_cells(game, 9, 0)  # SW
