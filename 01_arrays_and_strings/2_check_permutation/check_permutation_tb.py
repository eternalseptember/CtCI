# Test case for "check permutation" problem.


from check_permutation import *


# yes, yes, no, no, no (case-sensitive)
set = [['saw', 'was'], ['cat', 'act'], ['nap', 'map'], ['swap', 'swamp'], ['God', 'dog']]

for pairs in set:
	str_1 = pairs[0]
	str_2 = pairs[1]
	if is_permutation(str_1, str_2):
		print('Yes: {0} and {1}'.format(str_1, str_2))
	else:
		print('No: {0} and {1}'.format(str_1, str_2))


