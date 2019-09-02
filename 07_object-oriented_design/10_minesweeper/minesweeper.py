"""
Design and implement a text-based Minesweeper game. Minesweeper is the classic
single-player computer game where an NxN grid has Bmines (or bombs) hidden
across the grid. The remaining cells are either blank or have a number behind
them. The numbers reflect the number of bombs in the surrounding eight cells.
The user then uncovers a cell. If it is a bomb, the player loses. If it is a
number, the number is exposed. If it is a blank cell, this cell and all
adjacent blank cells (up to and including the surrounding numeric cells) are
exposed. The player wins when all non-bomb cells are exposed. The player can
also flag certain places as potential bombs. This doesn't affect game play,
other than to block the user from accidentally clicking a cell that is thought
to have a bomb.
"""


class Cell():
    def __init__(self, is_bomb):
        self.bomb = is_bomb
        self.marked = False


    def is_bomb(self):
        return self.bomb


class Minesweeper():
    def __init__(self, size, num_of_mines):
        self.size = size
        self.num_of_mines = num_of_mines
        self.board = self.init_game_board(size)


    def init_game_board(self, size):
        # len(board) is row; len(board[0]) is col
        init_board = [
            [None for col in range(size)] for row in range(size)
            ]
        return init_board


    def choose_cell(self, row, col):
        # should reveal whether the cell is a bomb or not
        cell = self.board[row][col]
        if cell.bomb:
            print('bomb')
        return None








