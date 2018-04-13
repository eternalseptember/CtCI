# Bit manipulation approach


def next_sets_of_numbers(num):
    # convert number to binary

    smallest = get_next_smallest(bin_num)
    largest = get_next_largest(bin_num)

    return smallest, largest


def get_next_smallest(num):
    temp = num
    c0 = 0
    c1 = 0

    while (temp & 1 == 1):
        c0 += 1
        temp = (temp >> 1)

    if (temp == 0):
        return -1

    p = c0 + c1  # position of right-most non-trailing zero
    num = num & ((~0) << (p + 1))  # clears from bit p onwards

    mask = (1 << (c1 + 1)) - 1  # sequence of (c1 + 1) ones
    num = num | (mask << (c0 - 1))

    return num


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

    num = num | (1 << p)  # flip right-most non-trailing zero
    num = num & (~((1 << p) - 1))  # clear all bits to the right of p
    num = num | ((1 << (c1 - 1)) - 1)  # insert (c1 - 1) ones on the right

    return num



