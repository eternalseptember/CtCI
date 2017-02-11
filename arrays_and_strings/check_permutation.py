"""
Given two strings, write a method to decide if one
is a permutation of the other.
"""


def is_permutation(str1, str2):
	if len(str1) != len(str2):
		return 0

	first_str = list(str1)

	for char in str2:
		try:
			first_str.remove(char)
		except ValueError:
			return 0

	return 1



# yes, yes, no, no
set = [['saw', 'was'], ['cat', 'act'], ['nap', 'map'], ['swap', 'swamp']]

for pairs in set:
	str_1 = pairs[0]
	str_2 = pairs[1]
	if is_permutation(str_1, str_2):
		print('Yes: {0} and {1}'.format(str_1, str_2))
	else:
		print('No: {0} and {1}'.format(str_1, str_2))

