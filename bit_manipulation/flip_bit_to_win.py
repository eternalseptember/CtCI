"""
You have an integer and you can flip exactly one bit from a 0 to a 1.
Write code to find the length of the longest sequence of ls you could
create.
"""


def longest_sequence_of_ones(num):
	# convert to binary
	bin_str = convert_to_binary(num)
	print(bin_str)

	longest_sequence = 0

	# for all zeros, flip one at a time
	# count all segments of ones, store the largest

	return longest_sequence


def convert_to_binary(num):
	# return a string'ed version of the binary
	bin_digits = []
	quotient = num

	while quotient > 0:
		rem = quotient % 2
		quotient = quotient // 2
		bin_digits.insert(0, rem)

	bin_string = ''.join(str(x) for x in bin_digits)

	return bin_string


# Testing
# Input: 1775 (11 0 111 0 1111)
# Output: 8 (11 0 111 1 1111)

inp = 1775
conseq_ones = longest_sequence_of_ones(inp)
print(conseq_ones)








