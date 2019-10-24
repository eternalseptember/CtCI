# Each cell in a minesweeper board.


class Cell():
    def __init__(self, is_mine=False, num_of_adj_mines=0, revealed=False):
        self.is_mine = is_mine
        self.num_of_adj_mines = num_of_adj_mines
        self.revealed = revealed
        self.flagged = False


    def __str__(self):
        if self.flagged:
            return '!'

        if self.revealed:
            if self.is_mine:
                return 'X'
            else:
                if self.num_of_adj_mines == 0:
                    return str(' ')
                else:
                    return str(self.num_of_adj_mines)
        else:
            return '-'


    def __repr__(self):
        if self.flagged:
            return '!'

        if self.revealed:
            if self.is_mine:
                return 'X'
            else:
                if self.num_of_adj_mines == 0:
                    return str(' ')
                else:
                    return str(self.num_of_adj_mines)
        else:
            return '-'

    def export_format(self):
        return '({0},{1},{2})'\
            .format(self.is_mine, self.num_of_adj_mines, self.revealed)


    def set_mine(self):
        self.is_mine = True

    def add_adj_mine(self):
        self.num_of_adj_mines += 1

    def is_blank(self):
        # Returns the opposite of reveal().
        return (not self.is_mine) and (self.num_of_adj_mines == 0)

    def is_revealed(self):
        return self.revealed

    def flag(self):
        self.flagged = True

    def unflag(self):
        self.flagged = False

    def reveal(self):
        self.revealed = True

        if self.is_mine:
            return True
        elif self.num_of_adj_mines > 0:
            return str(self.num_of_adj_mines)
        else:
            # Returns the opposite of is_blank().
            return False

