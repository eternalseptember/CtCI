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


