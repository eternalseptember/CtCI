"""
Is Unique: Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
"""


def check_characters(str):
	# ASCII has 128 characters
	if len(str) > 128:
		return False
	# extended ASCII has 256 characters


	already_stored = {}
	for char in str:
		if char not in already_stored:
			already_stored[char] = 1
		else:
			return False
	return True


test_str = ['cat', 'dog', 'squirrel']

for str in test_str:
	print(check_characters(str))


