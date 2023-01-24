# Optimal solution
# Integer.BYTES = 32?
# O(b) time, where b is the length of the sequence.
# O(1) memory.


def longest_sequence_of_ones(num):
	if num == -1:
		# -1 in binary is a string of all ones.
		# This is already the longest sequence.
		return "No bits are flipped."

	current_length = 0
	previous_length = 0
	max_length = 1  # We can always have a sequence of at least one 1.

	while (num != 0):
		if ((num & 1) == 1):
			# current bit is a 1
			current_length += 1
		elif ((num & 1) == 0):
			# current bit is a 0
			# if next bit is 0, update to 0
			# if next bit is 1, update current_length
			if ((num & 2) == 0):
				previous_length = 0
			else:
				previous_length = current_length

			current_length = 0

		max_length = max(previous_length + current_length + 1, max_length)
		num = num >> 1

	return max_length


