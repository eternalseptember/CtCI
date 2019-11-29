from minesweeper import *


game = Minesweeper(10, 10)
game.import_board("game01.txt")
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
game.choose_cell(1, 3)
game.choose_cell(1, 4)
game.choose_cell(0, 4, 'F')
game.choose_cell(0, 3)
game.choose_cell(2, 2)
game.choose_cell(1, 2)
game.choose_cell(1, 1, 'F')
game.choose_cell(0, 2)
game.choose_cell(0, 1)
game.choose_cell(0, 0)
game.choose_cell(1, 0)

