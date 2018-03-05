# The solution provided.


def insert_bits(N, M, i, j):
    # Create a mask to clear bits i through j in n.
    # Example: i = 2, j = 4. Result should be 11100011.

    all_ones = ~0
    print(all_ones)  # -1??

    # 1's before position j, then 0's. left = 11100000
    left = all_ones << (j + 1)
    print(left)

    return None




