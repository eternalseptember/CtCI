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
    def __init__(self, is_mine, num_of_neighbor_mines):
        self.mine = is_mine
        self.num_of_neighbor_mines = num_of_neighbor_mines
        self.flagged = False
        self.revealed = False


    def is_mine(self):
        return self.mine

    def flag(self):
        self.flagged = True

    def unflag(self):
        self.flagged = False


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


    def choose_cell(self, row, col):
        # should reveal whether the cell is a mine or not
        cell = self.board[row][col]
        if cell.mine:
            print('mine')
        return None








