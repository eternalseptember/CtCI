# The solution provided.


def insert_bits(N, M, i, j):
    # Create a mask to clear bits i through j in n.

    # since the problem states 32-bit numbers
    all_ones = 0b1111111111111111111111111111111
    format_print('all ones', all_ones)

    # 1's before position j, then 0's.
    left = all_ones << (j + 1)
    format_print('left mask', left)

    # 1's after position i.
    right = (1 << i) - 1
    format_print('right mask', right)

    # All 1's, except for 0's between i and j.
    mask = left | right
    format_print('mask', mask)

    # Clear bits j through i, then put m in there.
    n_cleared = N & mask  # Clear bits j through i.
    m_shifted = M << i  # Move m into correct position.

    # OR them.
    result = n_cleared | m_shifted
    format_print('result', result)
    return result


def format_print(text, item):
    # print('{0:032b}'.format(item))  # 32-bit numbers
    # print('{0:>12}: {1:08b}'.format(text, item))
    print('{0:>12}: {1:b}'.format(text, item))



