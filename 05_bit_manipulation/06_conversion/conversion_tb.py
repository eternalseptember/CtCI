from conversion import *
# from conversion_sol import *


# Test case 1
# Expected result: 2
int_a = 29  # 11101
int_b = 15  # 01111
result = number_of_bits_to_flip(int_a, int_b)
print(result)


# Test case 2
# Expected result = 0
int_a = 0  # 0
int_b = 0  # 0
result = number_of_bits_to_flip(int_a, int_b)
print(result)


# Test case 3
# Expected result = 1
int_a = 1  # 1
int_b = 0  # 0
result = number_of_bits_to_flip(int_a, int_b)
print(result)


