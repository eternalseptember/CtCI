# Bit manipulation approach


def next_sets_of_numbers(num):
    # convert number to binary

    smallest = get_next_smallest(bin_num)
    largest = get_next_largest(bin_num)

    return smallest, largest


def get_next_smallest(num):
    c = num
    c0 = 0
    c1 = 0

    while (((c & 1) == 0) and (c != 0)):
        c0 += 1
        c >> 1

    while ((c & 1) == 0):
        c1 += 1
        c >>= 1

    #

    return None


def get_next_largest(num):
    return None



