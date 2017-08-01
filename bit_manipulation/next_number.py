"""
Given a positive integer, print the next smallest and the next largest
number that have the same number of 1 bits in their binary representation.
"""


def next_sets_of_numbers(num):
	bin_num = convert_to_binary(num)
	print(bin_num)

	smallest = get_next_smallest(bin_num)
	largest = get_next_largest(bin_num)

	return smallest, largest


def get_next_smallest(bin_num):
	# expected input: binary representation of number
	# flip 0->1 and 1->0
	# in other words, exchange a 0 and 1

	# before flipping:
	# if the last 1 is like this:
	# x x 1 0 x x
	# then...
	# x x 0 1 x x

	# it's easier to do if the binary number is flipped
	bin_num = bin_num[::-1]
	bin_size = len(bin_num)

	# after flipping:
	# x x 0 1 x x
	# then...
	# x x 1 0 x x

	for i in range(0, bin_size):
		one_index = None
		zero_index = None
		if bin_num[i] == 1:
			one_index = i


	# case:
	# 01: 1

	return bin_num[::-1]


def get_next_largest(bin_num):
	# expected input: binary representation of number
	# flip 0->1 and 1->0
	# in other words, exchange a 0 and 1

	# if the last 1 is like this:
	# x x 0 1 x x
	# then...
	# x x 1 0 x x

	return None


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


