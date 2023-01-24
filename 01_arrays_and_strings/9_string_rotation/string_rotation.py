"""
Assume you have a method isSubstring which checks if one word is a
substring of another. Given two strings, s1 and s2, write code to
check if s2 is a rotation of s1 using only one call to isSubstring.
"""


def is_substring(str1, str2):
	"""
	If is_substring runs in O(A+B) time (on strings of length A and B),
	then the runtime is O(N).
	"""
	if len(str1) != len(str2):
		return False

	length = len(str2)
	for index in range(1, length):
		part1 = str1[:index]
		part2 = str1[index:]
		new_string = part2 + part1

		if new_string == str2:
			return True

	return False

