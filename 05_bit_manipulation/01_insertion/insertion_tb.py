# from insertion import *
from insertion_sol import *


# Test case 0: N = 10000010100
# Example works when all ones can be set to 0b111.
# left  = 11100000
# right = 00000011
# mask  = 11100011
N = 10000000000
M = 101
i = 2
j = 4

new_bit = insert_bits(N, M, i, j)
print()



# Test case 1: N = 10001001100
N = 10000000000
M = 10011
i = 2
j = 6

new_bit = insert_bits(N, M, i, j)
# result is being printed in the main function as it's being tested
# print(new_bit)


