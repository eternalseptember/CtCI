# Brute force solution


def longest_sequence_of_ones(num):
    if num == -1:
        # -1 in binary is a string of all ones.
        # This is already the longest sequence.
        # return Integer.bytes * 8
        # 32?
        return "all ones"


    sequences = get_alternating_sequences(num)
    return find_longest_sequence(sequences)


def get_alternating_sequences(num):
    seq_list = []
    return seq_list


def find_longest_sequences(seq_list):
    max_seq = 1

    return max_seq


