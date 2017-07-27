"""
You are given two 32-bit numbers, N and M, and two bit positions, i and j.
Write a method to insert M into N such that M starts at bit j and ends at
bit i. You can assume that the bits j through i have enough space to fit
all of M. That is, if M = 10011, you can assume that there are at least 5
bits between j and i. You would not, for example, have j = 3 and i = 2,
because M could not fully fit between bit 3 and bit 2.
"""


def insert_bits(N, M, i, j):
	start_pos = j
	end_pos = i

	M_bit = [int(bit) for bit in str(M)]
	N_bit =  [int(bit) for bit in str(N)]
	N_bit = N_bit[::-1]



	# Format the result to return
	N_bit = N_bit[::-1]
	N_str = ''.join(str(bit) for bit in N_bit)

	return int(N_str)


# Test case 1
# expected result: N = 10001001100
N = 10000000000
M = 10011
i = 2
j = 6

new_bit = insert_bits(N, M, i, j)
print(new_bit)



