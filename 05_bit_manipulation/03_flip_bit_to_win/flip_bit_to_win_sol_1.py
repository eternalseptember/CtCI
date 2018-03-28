# Brute force solution


def longest_sequence_of_ones(num):
    if num == -1:
        # -1 in binary is a string of all ones.
        # This is already the longest sequence.
        # return Integer.bytes * 8 = 32?
        return 32

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
    for i in range(32):
        if ((num & 1) != searching_for):
            seq_list.append(counter)
            searching_for = num & 1  # Flip 1 to 0 or 0 to 1
            counter = 0

        counter += 1
        # n >>>= 1

    return seq_list


def find_longest_sequence(seq_list):
    max_seq = 1

    return max_seq


