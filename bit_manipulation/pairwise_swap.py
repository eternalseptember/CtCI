"""
Write a program to swap odd and even bits in an integer with as few
instructions as possible (e.g., bit 0 and bit 1 are swapped, bit 2
and bit 3 are swapped, and so on).
"""


def pairwise_swap(num):
	# convert to integer

	# swap
	swapped_bits = ''

	return swapped_bits


def convert_to_binary(num):
	bin_digits = []
	quotient = num

	while quotient > 0:
		rem = quotient % 2
		quotient = quotient // 2
		bin_digits.insert(0, rem)

	return bin_digits


# Testing


