# Test cases for flip bit problem.


from flip_bit_to_win import *
# from flip_bit_to_win_sol_1 import *


# Test case 1
# Input: 1775 (11 0 111 0 1111)
# Output: 8 (11 0 111 1 1111)
print(longest_sequence_of_ones(1775))


# Test case 2
# Input: 0
# Output: 1
print(longest_sequence_of_ones(0))


# Test case 3
# Input: -1
# Output: "No bits are flipped."
print(longest_sequence_of_ones(-1))


# Test case 4
# Input: 14 (1110)
# Output: 4
print(longest_sequence_of_ones(14))


# Test case 5
# Input: 7 (0111)
# Output: 4
print(longest_sequence_of_ones(7))


