# Brute force solution


def longest_sequence_of_ones(num):
    if num == -1:
        # -1 in binary is a string of all ones.
        # return integer.bytes * 8
        return "all ones"
        

    sequences = get_alternating_sequences(num)
    return None


def get_alternating_sequences(num):
    return []


