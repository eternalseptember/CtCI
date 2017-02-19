"""
There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one
edit (or two edits) away.
"""


def one_away(str1, str2):
	return True



# true, true, true, false
str_1_set = ['pale', 'pales', 'pale', 'pale']
str_2_set = ['ple', 'pale', 'bale', 'bake']

sets = 4
for i in range(sets):
	str_1 = str_1_set[i]
	str_2 = str_2_set[i]

	result = one_away(str_1, str_2)
	print(result)


