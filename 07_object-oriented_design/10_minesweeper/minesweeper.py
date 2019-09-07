"""
Design and implement a text-based Minesweeper game. Minesweeper is the classic
single-player computer game where an NxN grid has B mines (or mines) hidden
across the grid. The remaining cells are either blank or have a number behind
them. The numbers reflect the number of mines in the surrounding eight cells.
The user then uncovers a cell. If it is a mine, the player loses. If it is a
number, the number is exposed. If it is a blank cell, this cell and all
adjacent blank cells (up to and including the surrounding numeric cells) are
exposed. The player wins when all non-mine cells are exposed. The player can
also flag certain places as potential mines. This doesn't affect game play,
other than to block the user from accidentally clicking a cell that is thought
to have a mine.
"""


class Cell():
    def __init__(self):
        self.is_mine = False
        self.num_of_adj_mines = 0
        self.flagged = False
        self.revealed = False


    def __str__(self):
        if self.flagged:
            return ' ! '
        if not self.revealed:
            return ' - '

        return str(self.num_of_adj_mines)


    def set_mine(self):
        self.is_mine = True

    def count_adj_mines(self):
        self.num_of_adj_mines += 1

    def is_mine(self):
        return self.is_mine

    def flag(self):
        self.flagged = True

    def unflag(self):
        self.flagged = False

    def reveal(self):
        if self.is_mine:
            print('bomb')
        elif self.num_of_adj_mines == 0:
            print('reveal connected blank cells and numeric cells')
        else:
            print('reveal the number of adj mines')




class Minesweeper():
    def __init__(self, size, num_of_mines):
        self.size = size
        self.num_of_mines = num_of_mines
        self.board = self.init_game_board(size)
        self.cells_revealed = 0


    def init_game_board(self, size):
        # len(board) is row; len(board[0]) is col
        # Creates a blank board.
        init_board = [
            [None for col in range(size)] for row in range(size)
            ]
        return init_board


    def print_board(self):
        for row in range(self.size):
            for col in range(self.size):
                piece = self.board[row][col]

                if piece is None:
                    print('   ')
                else:
                    print(' {0} '.format(piece))
            print()


    def begin_game(self):
        # First click is always a blank cell.
        print('begin game')
        row = int(input('Row: '))
        col = int(input('Col: '))
        self.choose_cell(row, col, True)


    def choose_cell(self, row, col, init_game=False):
        # The first chosen cell is always blank.


        # If the cell is not flagged and hasn't already been revealed,
        # reveal what's in the cell.
        cell = self.board[row][col]
        if cell.is_mine:
            print('mine')
        return None








