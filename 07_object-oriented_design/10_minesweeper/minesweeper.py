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


from minesweeper_cell import *


class Minesweeper():
    def __init__(self, size, num_of_mines):
        self.size = size
        self.num_of_mines = num_of_mines
        self.board = self.init_game_board(size)
        self.mines_placed = False
        self.max_cells_revealed = size * size - num_of_mines
        self.num_cells_revealed = 0


    def init_game_board(self, size):
        # len(board) is row; len(board[0]) is col
        # Creates a blank board.
        init_board = [
            [Cell() for col in range(size)] for row in range(size)
            ]
        return init_board


    def print_board(self, reveal=False):
        # for formatting purposes, assume that size is < 100.
        for printed_row_num in range(self.size + 1):

            # Print column numbers.
            if printed_row_num == 0:
                # Top left corner.
                print('  ', end=' ')

                # Column numbers.
                for col_num in range(self.size):
                    print('{0:>2d}'.format(col_num), end=' ')

                print()
                continue

            # Print game board.
            row = printed_row_num - 1

            for printed_col_num in range(self.size + 1):
                # Print row numbers.
                if printed_col_num == 0:
                    print('{0:>2d}'.format(row), end=' ')
                    continue

                # Print game board.
                col = printed_col_num - 1
                piece = self.board[row][col]

                if reveal:
                    piece.reveal()

                print('{0:>2}'.format(str(piece)), end=' ')

            print()
        print()


    def begin_game(self):
        # The first chosen cell is always blank.
        self.print_board()
        print('Begin Game')
        row = int(input('Row: '))
        col = int(input('Col: '))
        self.choose_cell(row, col)


    def choose_cell(self, row, col, option='R'):
        # Return True if the cell can be chosen.
        # Return False if the cell can't be chosen (flagged or was revealed).
        # Options: 'R' for reveal (default), 'F' for flag, and 'U' for unflag.

        if self.is_valid(row, col):
            if option == 'R':
                # The first chosen cell is always blank.
                if self.mines_placed is False:
                    self.set_board(row, col)
                    self.reveal_neighboring_cells(row, col)

                # The rest of the game.
                else:
                    cell = self.board[row][col]
                    # Flag? Click?

            elif option == 'F':
                print('flag')
            elif option == 'U':
                print('unflag')

            self.print_board()
            return True
        else:
            return False


    def is_valid(self, row, col, option='R'):
        # Options: 'R' for reveal (default), 'F' for flag, and 'U' for unflag.

        # Check that cell picked is within bounds.
        if (row < 0) or (row >= self.size):
            return False
        if (col < 0) or (col >= self.size):
            return False

        # Check the cell.
        cell = self.board[row][col]
        if cell.flagged or cell.revealed:
            return False

        return True


    def list_neighboring_cells(self, row, col):
        # Return a list of valid neighboring cells.
        neighboring_cells = []

        N = row - 1
        S = row + 1
        W = col - 1
        E = col + 1

        check_N = False if (N < 0) else True
        check_S = False if (S >= self.size) else True
        check_W = False if (W < 0) else True
        check_E = False if (E >= self.size) else True

        # Check diagonals.
        if check_N and check_W:
            coords = [(N, col), (row, W), (N, W)]
            for coord in coords:
                if coord not in neighboring_cells:
                    neighboring_cells.append(coord)

        if check_N and check_E:
            coords = [(N, col), (row, E), (N, E)]
            for coord in coords:
                if coord not in neighboring_cells:
                    neighboring_cells.append(coord)

        if check_S and check_W:
            coords = [(S, col), (row, W), (S, W)]
            for coord in coords:
                if coord not in neighboring_cells:
                    neighboring_cells.append(coord)

        if check_S and check_E:
            coords = [(S, col), (row, E), (S, E)]
            for coord in coords:
                if coord not in neighboring_cells:
                    neighboring_cells.append(coord)

        return neighboring_cells


    def set_board(self, row, col):
        # The first chosen cell is always blank.
        cell = self.board[row][col]
        cell.reveal()
        self.num_cells_revealed += 1

        # Which means neighboring cells have no mines.
        # Remove them from the possible locations to place bombs.

        # Create a list of all board spaces coordinates.
        all_cells = []
        for row_num in range(self.size):
            for col_num in range(self.size):
                all_cells.append((row_num, col_num))

        # Remove selected cell and neighboring cells.
        all_cells.remove((row, col))
        neighboring_cells = self.list_neighboring_cells(row, col)
        for neighboring_cell in neighboring_cells:
            all_cells.remove(neighboring_cell)

        # Shuffle list of remaining board spaces.
        from random import randrange
        num_of_cells = len(all_cells)
        shuffled_list = []

        while num_of_cells > 0:
            rand_num = randrange(num_of_cells)
            shuffled_list.append(all_cells.pop(rand_num))
            num_of_cells -= 1

        # Pick num_of_mines from the top of the list.
        # Plug the unpacked tuple into the place_mines function.
        for i in range(self.num_of_mines):
            mine = shuffled_list.pop()
            row, col = mine
            self.place_mines(row, col)

        self.mines_placed = True


    def place_mines(self, row, col):
        cell = self.board[row][col]
        cell.set_mine()

        # Then update surrounding cell's adj_mine count.
        neighboring_cells = self.list_neighboring_cells(row, col)

        for neighboring_cell in neighboring_cells:
            neigh_row, neigh_col = neighboring_cell
            neigh_cell = self.board[neigh_row][neigh_col]
            neigh_cell.add_adj_mine()


    def reveal_neighboring_cells(self, row, col):
        # When the player chooses a blank cells, reveal adjacent blank cells
        # and surrounding number cells.
        neigh_cells_list = self.list_neighboring_cells(row, col)

        for cell in neigh_cells_list:
            neigh_row, neigh_col = cell
            neigh_cell = self.board[neigh_row][neigh_col]

            if not neigh_cell.is_revealed():
                has_something = neigh_cell.reveal()
                self.num_cells_revealed += 1

                if not has_something:
                    new_cells = self.list_neighboring_cells(neigh_row, neigh_col)

                    for new_cell in new_cells:
                        if new_cell not in neigh_cells_list:
                            neigh_cells_list.append(new_cell)















