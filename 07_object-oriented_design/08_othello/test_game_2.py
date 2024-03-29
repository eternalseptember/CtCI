# Testing indivdual player actions during the game.
# This file tries to reach an end-game state.


def place_piece(self, player, row, col):
	self.print_move_checks()
	player.place_piece(row, col)
	self.move_checks.clear()


# Black goes first.
active_player = self.players[0]
place_piece(self, active_player, 2, 3)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 4, 2)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 5, 4)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 4, 5)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 5, 3)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 6, 4)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 5, 5)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 2, 4)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 1, 4)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 0, 4)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 4, 6)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 4, 7)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 3, 5)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 5, 2)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 5, 1)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 2, 2)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 7, 4)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 6, 3)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 7, 3)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 6, 2)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 1, 3)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 6, 5)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 7, 5)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 0, 3)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 3, 2)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 5, 6)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 5, 7)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 6, 7)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 4, 1)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 5, 0)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 6, 1)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 4, 0)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 1, 2)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 0, 2)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 3, 1)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 7, 2)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 7, 1)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 2, 5)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 1, 5)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 1, 6)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 2, 1)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 6, 6)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 0, 5)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 6, 0)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 1, 1)

# White's turn.
active_player = self.players[1]
place_piece(self, active_player, 1, 0)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 0, 1)

# White's turn.
active_player = self.players[1]
can_pass = active_player.pass_turn()
print('white can pass turn?')
print(can_pass)

# Black's turn
active_player = self.players[0]
place_piece(self, active_player, 1, 7)


"""
# White's turn.
active_player = self.players[1]
can_pass = active_player.pass_turn()
print('white can pass turn?')
print(can_pass)


# Black's turn
active_player = self.players[0]
can_pass = active_player.pass_turn()
print('black can pass turn?')
print(can_pass)
"""






