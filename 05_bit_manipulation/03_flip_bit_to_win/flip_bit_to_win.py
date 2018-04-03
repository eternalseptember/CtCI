"""
You have an integer and you can flip exactly one bit from a 0 to a 1.
Write code to find the length of the longest sequence of ls you could
create.
"""


def longest_sequence_of_ones(num):
    if num == -1:
        return "No bits are flipped."


    # convert to binary
    bin_str = bin(num)[2:]  # gets the binary string
    bin_str = [int(bit) for bit in list(bin_str)]
    bin_str_len = len(bin_str)


    # counts zeros and gets their indexes
    num_of_zeros = 0
    zero_indexes = []

    for i in range(bin_str_len):
        if bin_str[i] == 0:
            zero_indexes.append(i)
            num_of_zeros += 1


    # finds the longest sequence of ones
    longest_sequence = 0

    for zero in range(num_of_zeros):
        flip_index = zero_indexes[zero]

        # flipping the specified index to one
        bin_str_flipped = bin_str[:]
        bin_str_flipped[flip_index] = 1

        # count all segments of ones and store the largest
        conseq_ones = 0

        for bit in bin_str_flipped:
            if bit == 1:
                conseq_ones += 1
            else:
                if conseq_ones > longest_sequence:
                    longest_sequence = conseq_ones
                conseq_ones = 0

        # check the last sequence
        if conseq_ones > longest_sequence:
            longest_sequence = conseq_ones


    return longest_sequence







