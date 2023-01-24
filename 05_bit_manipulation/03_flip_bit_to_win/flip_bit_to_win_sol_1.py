# Brute force solution
# Integer.BYTES = 32?
# O(b) time and O(b) memory, where b is the length of the sequence.


def longest_sequence_of_ones(num):
	if num == -1:
		# -1 in binary is a string of all ones.
		# This is already the longest sequence.
		return "No bits are flipped."

	sequences = get_alternating_sequences(num)
	return find_longest_sequence(sequences)


def get_alternating_sequences(num):
	# Returns a list of the sixes of the sequences. The sequence starts
	# off with the number of 0's (which might be 0) and then the
	# alternates with the counts of each value.
	seq_list = []

	searching_for = 0
	counter = 0

	# i in range Integer.BYTES
	for i in range(32 * 8):
		if ((num & 1) != searching_for):
			seq_list.append(counter)
			searching_for = num & 1  # Flip [1 to 0] or [0 to 1].
			counter = 0

		counter += 1

		# num >>>= 1; >>> is zero-fill right shift
		num = num >> 1

	seq_list.append(counter)

	return seq_list


def find_longest_sequence(seq_list):
	# Given the lengths of alternating sequence of 0's and 1's,
	# find the longest one we can build.
	max_seq = 1

	for i in range(0, len(seq_list), 2):
		zeros_seq = seq_list[i]

		if (i - 1) >= 0:
			ones_seq_right = seq_list[i - 1]
		else:
			ones_seq_right = 0

		if (i + 1) < len(seq_list):
			ones_seq_left = seq_list[i + 1]
		else:
			ones_seq_left = 0

		this_seq = 0
		if zeros_seq == 1:
			# can merge
			this_seq = ones_seq_left + 1 + ones_seq_right
		elif zeros_seq > 1:
			# just add a zero to either side
			this_seq = 1 + max(ones_seq_right, ones_seq_left)
		elif zeros_seq == 0:
			# no zero, but take either side
			this_seq = max(ones_seq_right, ones_seq_left)

		max_seq = max(this_seq, max_seq)

	return max_seq


