"""
Write an algorithm such that if an element in an MxN matrix
is 0, its entire row and column are set to 0.
"""


def zero_matrix(M, N, matrix):
    zero_row = []
    zero_col = []

    # find the zeros
    for row in range(M):
        for col in range(N):
            if matrix[row][col] == 0:
                zero_row.append(row)
                zero_col.append(col)

    # set entire row and column to zero
    for row in range(M):
        for col in range(N):
            if (row in zero_row) or (col in zero_col):
                matrix[row][col] = 0

    return matrix


M = 4  # row
N = 5  # col
matrix = [[3, 4, 5, 6, 7], [0, 1, 2, 4, 6], [3, 2, 4, 5, 1], [8, 4, 2, 1, 0]]

print('Original matrix:')
for row in matrix:
    print(row)
print()


zeroed_matrix = zero_matrix(M, N, matrix)
print('Zeroed matrix:')
for row in zeroed_matrix:
    print(row)

