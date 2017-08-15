"""
Write a function to determine the number of bits you would need to
flip to convert integer A to integer B.
"""


def number_of_bits_to_flip(int_a, int_b):
	bin_a = int_to_binary(int_a)
	bin_b = int_to_binary(int_b)

	# pad leading zeros
	bin_a_len = len(bin_a)
	bin_b_len = len(bin_b)

	if bin_a_len > bin_b_len:
		# pad bin_b
		padding_zeros = bin_a_len - bin_b_len
		for i in range(padding_zeros):
			bin_b.insert(0, 0)
	elif bin_b_len > bin_a_len:
		# pad bin_a
		padding_zeros = bin_b_len - bin_a_len
		for i in range(padding_zeros):
			bin_a.insert(0, 0)

	print(bin_a)
	print(bin_b)

	# lengths should be equal
	num_to_flip = 0


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


