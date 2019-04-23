# Functions that print the state of the game.
# Meant to be imported into the main Othello class.


def print_board(self):
    for row in range(8):
        for col in range(8):
            piece = self.board[row][col]
            if piece is None:
                if (row, col) in self.playable_spots:
                    print(' - ', end='')
                else:
                    print(' . ', end='')
            else:
                print(' {0} '.format(piece), end='')
        print()

    print("*****************************************")


def print_playable_spots(self):
    print('Pieces played: {0}'.format(self.pieces_played))
    print('Playable spots:', end=' ')
    for spot in self.playable_spots:
        print(spot, end=' ')
    print()


def print_score(self):
    print("************** Final Score **************")
    print("Black: {0}".format(self.black_count))
    print("White: {0}".format(self.white_count))



