"""
Write a program to swap odd and even bits in an integer with as few
instructions as possible (e.g., bit 0 and bit 1 are swapped, bit 2
and bit 3 are swapped, and so on).
"""


def pairwise_swap(num):
	# convert to integer
	bit_num = bin(num)[2:]
	bit_num = [int(bit) for bit in bit_num]

	# if the integer has an odd number of bits, put a zero bit in front
	if len(bit_num) % 2 == 1:
		bit_num.insert(0, 0)

	# swap
	bit_len = len(bit_num)

	for bit_1 in range(0, bit_len, 2):
		# LSB numbering; bit_1 is left and bit_0 is right
		bit_0 = bit_1 + 1
		bit_num[bit_1], bit_num[bit_0] = bit_num[bit_0], bit_num[bit_1]

	res_str = ''.join(str(bit) for bit in bit_num)

	return int(res_str, 2)







