"""
Write a function to determine the number of bits you would need to
flip to convert integer A to integer B.
"""


def number_of_bits_to_flip(int_a, int_b):
    bin_a = bin(int_a)[2:]
    bin_b = bin(int_b)[2:]

    # pad leading zeros
    bin_a_len = len(bin_a)
    bin_b_len = len(bin_b)

    if bin_a_len > bin_b_len:
        bin_b = bin_b.zfill(bin_a_len)
    elif bin_a_len < bin_b_len:
        bin_a = bin_a.zfill(bin_b_len)


    # lengths should be equal
    num_to_flip = 0
    for i in range(bin_a_len):
        if bin_a[i] != bin_b[i]:
            num_to_flip += 1

    return num_to_flip






