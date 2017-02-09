"""
Is Unique: Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
"""


def check_characters(str):
	already_stored = {}
	for char in str:
		if char not in already_stored:
			already_stored[char] = 1
		else:
			return 0
	return 1


test_str = ['cat', 'dog', 'squirrel']

for str in test_str:
	if check_characters(str):
		print('True. All characters are unique')
	else:
		print('False. Some characters repeat.')


