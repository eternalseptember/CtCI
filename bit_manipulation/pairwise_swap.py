"""
Write a program to swap odd and even bits in an integer with as few
instructions as possible (e.g., bit 0 and bit 1 are swapped, bit 2
and bit 3 are swapped, and so on).
"""


def pairwise_swap(num):
	# convert to integer
	bit_num = convert_to_binary(num)

	# if the integer has an odd number of bits, put a zero bit in front
	if len(bit_num) % 2 == 1:
		bit_num.insert(0, 0)

	# swap
	bit_pairs = len(bit_num) // 2

	for pair in range(bit_pairs):
		# LSB numbering; bit_1 is left and bit_0 is right
		bit_1 = pair * 2
		bit_0 = bit_1 + 1

		bit_num[bit_1], bit_num[bit_0] = bit_num[bit_0], bit_num[bit_1]
	
	return bit_num


def convert_to_binary(num):
	bin_digits = []
	quotient = num

	while quotient > 0:
		rem = quotient % 2
		quotient = quotient // 2
		bin_digits.insert(0, rem)

	return bin_digits


# Testing
# Test case 1: 101010 <-> 010101
num = 42
results = pairwise_swap(num)
print(results)


# Test case 2: 111 or 0111 <-> 1011 
num = 7
results = pairwise_swap(num)
print(results)



