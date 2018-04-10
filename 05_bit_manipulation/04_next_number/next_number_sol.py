# Bit manipulation approach


def next_sets_of_numbers(num):
    # convert number to binary

    smallest = get_next_smallest(bin_num)
    largest = get_next_largest(bin_num)

    return smallest, largest


def get_next_smallest(num):

    return None


def get_next_largest(num):
    c = num
    c0 = 0
    c1 = 0

    while (((c & 1) == 0) and (c != 0)):
        c0 += 1
        c >> 1

    while ((c & 1) == 0):
        c1 += 1
        c >>= 1


    p = c0 + c1  # position of right-most non-trailing zero

    # Error if n == 11.. 1100... 00,
    # then there is no bigger number with the same number of 1's.
    if (p == 31) or (p == 0):
        return -1


    return None



