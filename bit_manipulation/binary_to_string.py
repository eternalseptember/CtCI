"""
Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a
double, print the binary representation. If the number cannot be
represented accurately in binary with at most 32 characters, print "ERROR".
"""


def binary_to_string(num):
	bin_result = []
	div_result = num


	# testing with integer first
	while ((div_result > 0) and (len(bin_result) < 32)):	
		rem = div_result % 2
		div_result = div_result // 2
		bin_result.insert(0, rem)





	if (div_result == 0) or (len(bin_result) <= 32):
		bin_string = ''.join(str(x) for x in bin_result)
		return bin_string
	else:
		return None


def binary_to_int(bin_str):
	bin_list = []
	int_total = 0
	bit_pos = 0

	for bit in list(bin_str):
		bin_list.append(int(bit))

	while len(bin_list) > 0:
		current_bit = bin_list.pop()
		int_total += (current_bit * 2**bit_pos)
		bit_pos += 1

	return int_total


# Test case 1: how to approach this problem using integers
# Expected result: 10

inp = 2
result_1 = binary_to_string(inp)
print(result_1)

result_2 = binary_to_int(result_1)
print(result_2)



"""
# Test case 2
# inp = 0.72
inp = 0.893
print(binary_to_string(inp))
"""



