# from conversion import *
from conversion_sol import *


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


# Test case 4
# Expected result = 1
int_a = 31  # 11111
int_b = 30  # 11110
result = number_of_bits_to_flip(int_a, int_b)
print(result)



# Test case 5
# Expected result = 5
int_a = 31  # 11111
int_b = 0  # 00000
result = number_of_bits_to_flip(int_a, int_b)
print(result)


# Test case 6
# Expected result = 5
int_a = 24  # 11000
int_b = 7  # 00111
result = number_of_bits_to_flip(int_a, int_b)
print(result)


# Test case 7
# Expected result = 3
int_a = 25  # 11001
int_b = 30  # 11110
result = number_of_bits_to_flip(int_a, int_b)
print(result)

