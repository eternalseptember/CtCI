"""
You are given two 32-bit numbers, N and M, and two bit positions, i and j.
Write a method to insert M into N such that M starts at bit j and ends at
bit i. You can assume that the bits j through i have enough space to fit
all of M. That is, if M = 10011, you can assume that there are at least 5
bits between j and i. You would not, for example, have j = 3 and i = 2,
because M could not fully fit between bit 3 and bit 2.
"""


def insert_bits(N, M, i, j):
    M_bit = [int(bit) for bit in str(M)]
    N_bit = [int(bit) for bit in str(N)]

    # In python, item[0] = item[-0], which is the first item,
    # and item[-1] is the last item.
    # Flip everything while doing the insert, then flip the final result.
    start_pos = i  # i is lower index
    end_pos = j
    M_bit = M_bit[::-1]
    N_bit = N_bit[::-1]

    # Going through N, which is longer than M
    for k in range(start_pos, end_pos+1):
        bit_to_be_inserted = M_bit.pop(0)
        N_bit[k] = bit_to_be_inserted

    # Format the result to return
    N_bit = N_bit[::-1]
    N_str = ''.join(str(bit) for bit in N_bit)

    return int(N_str)






