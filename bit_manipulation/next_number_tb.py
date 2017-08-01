"""
Brute force solution for first ~32'ish values.
"""


test_str = ['00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001', '01010', '01011', '01100', '01101', '01110', '01111', '10000', '10001', '10010', '10011', '10100', '10101', '10110', '10111', '11000', '11001', '11010', '11011', '11100', '11101', '11110', '11111']


bin_ones_count = {}

for bin_str in test_str:
	num_of_ones = bin_str.count('1')

	try:
		bin_ones_count[num_of_ones].append(bin_str)
	except:
		bin_ones_count[num_of_ones] = [bin_str]


for k,v in bin_ones_count.items():
	print('number of ones: {0}'.format(k))
	print(v)





