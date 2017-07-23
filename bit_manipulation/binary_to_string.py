"""
Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a
double, print the binary representation. If the number cannot be
represented accurately in binary with at most 32 characters, print "ERROR".
"""


def binary_to_string(num):
	bin_result = []
	div_result = num

	while ((div_result > 0) and (len(bin_result) < 32)):
		# // because testing with integer first
		rem = div_result % 2
		div_result = div_result // 2
		bin_result.insert(0, rem)


	if (div_result == 0) or (len(bin_result) <= 32):
		bin_string = ''.join(str(x) for x in bin_result)
		return bin_string
	else:
		return None


# Test case 1: how to approach this problem using integers
# Expected result: 10
inp = 2
print(binary_to_string(inp))

"""
# Test case 2
inp = 0.72
print(binary_to_string(inp))
"""




