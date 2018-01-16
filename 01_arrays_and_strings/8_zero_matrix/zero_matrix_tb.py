# Test case for "zero matrix" problem.


from zero_matrix import *


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

