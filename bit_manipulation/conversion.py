"""
Write a function to determine the number of bits you would need to
flip to convert integer A to integer B.
"""


def number_of_bits_to_flip(int_a, int_b):
	num_to_flip = 0

	bin_a = int_to_binary(int_a)
	bin_b = int_to_binary(int_b)

	print(bin_a)
	print(bin_b)

	# pad leading zeros

	return num_to_flip



def int_to_binary(num):
	bin_digits = []
	quotient = num

	while quotient > 0:
		rem = quotient % 2
		quotient = quotient // 2
		bin_digits.insert(0, rem)

	return bin_digits


# Testing
int_a = 29  # 11101
int_b = 15  # 01111
result = number_of_bits_to_flip(int_a, int_b)
print(result)


