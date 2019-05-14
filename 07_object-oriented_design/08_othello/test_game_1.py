# Testing indivdual player actions during the game, before player_turn
# function was written.
# File had two tabs in the begin_game function.


# Black goes first.
active_player = self.players[0]

# Testing spots.
self.test_spot(0, 0, str(active_player))  # False
self.test_spot(2, 3, str(active_player))  # True

# Place a piece.
self.print_move_checks()
active_player.place_piece(2, 3)
self.move_checks.clear()


# Switch turns and keep playing.
# White's turn.
active_player = self.players[1]
# self.print_playable_spots()

# Testing spots.
self.test_spot(0, 3, str(active_player))  # False
self.test_spot(4, 4, str(active_player))  # False
self.test_spot(4, 2, str(active_player))  # True

# Place a piece.
self.print_move_checks()
active_player.place_piece(4, 2)
self.move_checks.clear()


# Switch turns and keep playing.
# Black's turn
active_player = self.players[0]
self.test_spot(4, 1, str(active_player))  # False
self.test_spot(3, 2, str(active_player))  # False
self.test_spot(2, 4, str(active_player))  # False
self.test_spot(4, 1, str(active_player))  # False; repeat

# Place a piece.
self.print_move_checks()


