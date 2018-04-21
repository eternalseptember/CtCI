# Solution


"""
def number_of_bits_to_flip(int_a, int_b):
    count = 0

    c = int_a ^ int_b
    while (c != 0):
        count = count + (c & 1)
        c = c >> 1

    return count
"""



def number_of_bits_to_flip(int_a, int_b):
    count = 0

    c = int_a ^ int_b
    while (c != 0):
        count = count + (c & 1)
        c = c & (c - 1)

    return count



