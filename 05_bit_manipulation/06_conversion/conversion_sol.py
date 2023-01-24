# Solution


"""
def number_of_bits_to_flip(int_a, int_b):
	# count the number of bits in A xor B that are 1.
	count = 0

	c = int_a ^ int_b
	while (c != 0):
		# shifting c while checking the least significant bit
		count = count + (c & 1)
		c = c >> 1

	return count
"""



def number_of_bits_to_flip(int_a, int_b):
	count = 0

	c = int_a ^ int_b
	while (c != 0):
		# continuously flip the least significant bit and
		# count how long it takes c to reach 0
		count += 1
		c = c & (c - 1)  # clear the least significant bit in c.

	return count



