"""
You have an integer and you can flip exactly one bit from a 0 to a 1.
Write code to find the length of the longest sequence of ls you could
create.
"""


def longest_sequence_of_ones(num):
    # convert to binary
    bin_str = convert_to_binary(num)
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


def convert_to_binary(num):
    # return a string'ed version of the binary
    bin_digits = []
    quotient = num

    while quotient > 0:
        rem = quotient % 2
        quotient = quotient // 2
        bin_digits.insert(0, rem)

    #bin_string = ''.join(str(x) for x in bin_digits)

    return bin_digits








