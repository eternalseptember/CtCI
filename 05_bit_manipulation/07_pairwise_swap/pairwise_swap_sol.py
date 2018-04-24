# Solution


def pairwise_swap(num):
    # Mask odd bits with 0b101010...
    # Then shift them right by 1 to put them in even spots.
    # >>> is zero-fill right shift
    # ((num & 0xaaaaaaaa) >>> 1)
    # | 
    # ((num & 0x55555555) << 1)
    return None



