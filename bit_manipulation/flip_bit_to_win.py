"""
You have an integer and you can flip exactly one bit from a 0 to a 1.
Write code to find the length of the longest sequence of ls you could
create.
"""


def longest_sequence_of_ones(num):
	# convert to binary
	bin_str = convert_to_binary(num)

	longest_sequence = 0

	# for all zeros, flip one at a time
	# count all segments of ones, store the largest

	return longest_sequence


def convert_to_binary(num):
	# return a string'ed version of the binary
	binary = ''

	return binary


# Testing
# Input: 1775 (11 0 111 0 1111)
# Output: 8 (11 0 111 1 1111)

inp = 1775
conseq_ones = longest_sequence_of_ones(inp)
print(conseq_ones)








