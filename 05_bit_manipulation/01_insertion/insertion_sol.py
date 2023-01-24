# The solution provided.


def insert_bits(N, M, i, j):
	# Create a mask to clear bits i through j in n.
	# all_ones = (1 << 32) - 1  # string of 32 ones
	num_of_bits = len(str(N))
	all_ones = (1 << num_of_bits) - 1
	# format_print('all ones', all_ones)

	# 1's before position j, then 0's.
	left = all_ones << (j + 1)
	left = int(bin(left)[-num_of_bits:], 2)  # formatting mask
	# format_print('left mask', left)

	# 1's after position i.
	right = (1 << i) - 1
	# format_print('right mask', right)

	# All 1's, except for 0's between i and j.
	mask = left | right
	# format_print('mask', mask)

	# Clear bits j through i, then put m in there.
	new_N = int(str(N), 2)
	new_M = int(str(M), 2)
	n_cleared = new_N & mask  # Clear bits j through i.
	m_shifted = new_M << i  # Move m into correct position.

	# OR them.
	result = n_cleared | m_shifted
	# format_print('result', result)
	return result


def format_print(text, item):
	# For diagnostic purposes.
	# print('{0:>12}: {1:08b}'.format(text, item))
	print('{0:>12}: {1:b}'.format(text, item))



