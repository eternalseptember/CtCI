"""
Given a positive integer, print the next smallest and the next largest
number that have the same number of 1 bits in their binary representation.
"""


def next_sets_of_numbers(num):
	smallest = None
	largest = None

	bin_num = convert_to_binary(num)



	return smallest, largest


def convert_to_binary(num):
	# return a string'ed version of the binary
	bin_digits = []
	quotient = num

	while quotient > 0:
		rem = quotient % 2
		quotient = quotient // 2
		bin_digits.insert(0, rem)

	return bin_digits


# Testing
num = 10000
smallest, largest = next_sets_of_numbers(num)

# I think something special happens with 2 (10)


