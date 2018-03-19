# Test cases for the binary to string problem.


# from binary_to_string import *
from binary_to_string_sol import *


# Test case 0: How to approach this problem using integers?
# Expected result: 10
"""
inp = 2
result_1 = string_to_binary(inp)
print(result_1)

result_2 = binary_to_int(result_1)
print(result_2)
"""

# Test case 1
# Expected result = 0.101
inp = 0.625
print(string_to_binary(inp))
print()


# Test case 2
# Expected result = 0.00011(0011) repeating.
# So "Error".
inp = 0.1
print(string_to_binary(inp))



# Expected results?
"""
# Test case 3
# Expected result = ???
inp = 0.72
print(string_to_binary(inp))

# Test case 4
# Expected result = ???
inp = 0.893
print(string_to_binary(inp))
"""


