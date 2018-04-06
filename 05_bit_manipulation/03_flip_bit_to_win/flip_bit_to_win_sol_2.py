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


