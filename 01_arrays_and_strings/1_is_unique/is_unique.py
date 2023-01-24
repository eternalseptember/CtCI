"""
Is Unique: Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
"""

"""
def check_characters(test_str):
	# Time: O(n), where n is the length of the string.
	# Or O(1) since the for loop will never iterate more than 128 characters.
	# Space: O(1)
	#
	# If assuming the character set is not fixed:
	# Space: O(c)
	# Time: O(min(c, n)) or O(c)
	# where c is the size of the character set.

	# ASCII has 128 characters
	if len(test_str) > 128:
		return False
	# extended ASCII has 256 characters


	already_stored = {}
	for char in test_str:
		if char not in already_stored:
			already_stored[char] = 1
		else:
			return False
	return True
"""


def check_characters(test_str):
	# Can't use additional data structures.

	sorted_str = sorted(test_str)
	str_len = len(test_str)

	for char_index in range(1, str_len):
		prev_char = sorted_str[char_index - 1]
		curr_char = sorted_str[char_index]

		if prev_char == curr_char:
			return False

	return True


