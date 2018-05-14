# from insertion import *
from insertion_sol import *


# Test case 0: N = 10000010100
# Example works when all ones can be set to 0b111.
# left  = 11100000
# right = 00000011
# mask  = 11100011
# N = 10000000000
N = 10000011100  # the bits need to be cleared are marked
M = 101
i = 2
j = 4
new_bit = insert_bits(N, M, i, j)
print('{0:b}'.format(new_bit))


# Test case 1: N = 10000010100
N = 10000000000
M = 101
i = 2
j = 4
new_bit = insert_bits(N, M, i, j)
print('{0:b}'.format(new_bit))


# Test case 2: N = 10001001100
N = 10001111100  # the bits need to be cleared are marked
M = 10011
i = 2
j = 6
new_bit = insert_bits(N, M, i, j)
print('{0:b}'.format(new_bit))


# Test case 3: N = 10001001100
N = 10000000000
M = 10011
i = 2
j = 6
new_bit = insert_bits(N, M, i, j)
print('{0:b}'.format(new_bit))


# Test case 4: 10000010
# Even-numbered digits
N = 10101010
M = 0000
i = 2
j = 5
new_bit = insert_bits(N, M, i, j)
print('{0:b}'.format(new_bit))


# Test case 5: 1110110
# Clearing the whole thing
N = 1001001
M = 1110110
i = 0
j = 6
new_bit = insert_bits(N, M, i, j)
print('{0:b}'.format(new_bit))





