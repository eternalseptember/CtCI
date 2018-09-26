from puzzle_generator import *
from puzzle_solution import *


# Generate puzzle.
unsolved_puzzle = Puzzle(6)
# unsolved_puzzle.print_pieces()
# print()

# Solve puzzle.
puzzle_in_progress = Puzzle_Solution(6)
puzzle_in_progress.solve_puzzle(unsolved_puzzle)
print()
puzzle_in_progress.print_solution()


