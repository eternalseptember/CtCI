# Test cases for insertion problem.


# from insertion import *
from insertion_sol import *


# Test case 0: Testing the mask from the solution's example.
# left  = 11100000
# right = 00000011
# mask  = 11100011
N = 10000000000
M = 10011
i = 2
j = 4

new_bit = insert_bits(N, M, i, j)
# example works when all ones can be set to 0b111.
print()




# Test case 1
# expected result: N = 10001001100
N = 10000000000
M = 10011
i = 2
j = 6

new_bit = insert_bits(N, M, i, j)
# result is being printed in the main function as it's being tested
# print(new_bit)


