"""
Assume you have a method isSubstring which checks if one word is a
substring of another. Given two strings, s1 and s2, write code to
check if s2 is a rotation of s1 using only one call to isSubstring.
"""


def is_substring(str1, str2):
	return True


# print(is_substring('', ''))  #
print(is_substring('waterbottle', 'erbottlewat'))  # True
print(is_substring('nap', 'pan'))  # False
print(is_substring('racecar', 'cecarra'))  # True

