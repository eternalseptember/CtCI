# Test cases for the binary to string problem.


from binary_to_string import *
# from binary_to_string_sol import *


# Test case 1
# Expected result: 0.101
print(string_to_binary(0.625))


# Test case 2
# Expected result: ERROR. 0.00011(0011) repeating.
print(string_to_binary(0.1))


# Test case 3
# Expected result: ERROR. 0.101110000101...
print(string_to_binary(0.72))


# Test case 4
# Expected result: ERROR. 0.11100100100110...
print(string_to_binary(0.893))


# Test case 5
# Expected result: 0.001
print(string_to_binary(0.125))


# Test case 6
# Expected result: ERROR
print(string_to_binary(0))


# Test case 7
# Expected result: ERROR
print(string_to_binary(1))


# Test case 8
# Expected result: 0.1
print(string_to_binary(0.5))


# Test case 9
# Expected result: 0.01
print(string_to_binary(0.25))




