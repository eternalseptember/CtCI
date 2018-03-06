# The solution provided.


def insert_bits(N, M, i, j):
    # Create a mask to clear bits i through j in n.
    # Example: i = 2, j = 4. Result should be 11100011.

    all_ones = ~0
    print(all_ones)  # -1??

    # 1's before position j, then 0's.
    # left = 11100000
    left = all_ones << (j + 1)
    print(left)

    # 1's after position i.
    # right = 00000011
    right = (1 << i) - 1
    print(right)

    # All 1's, except for 0's between i and j.
    # mask = 11100011
    mask = left | right
    print(mask)

    # Clear bits j through i, then put m in there.
    n_cleared = N & mask  # Clear bits j through i.
    m_shifted = M << i  # Move m into correct position.

    # OR them.
    return n_cleared | m_shifted




