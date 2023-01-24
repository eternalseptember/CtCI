"""
Given a string, write a function to check if it is a permutation
of a palindrome. A palindrome is a word or phrase that is the same
forwards and backwards. A permutation is a rearrangement of
letters. The palindrome does not need to be limited to just
dictionary words.
"""


from collections import Counter


def check_palindrome(str):
	# Solution 1
	# O(N) time, where N is length of string
	str = str.lower().replace(' ', '')
	list_of_letters = Counter(str)

	odd = False
	for letter, count in list_of_letters.items():
		if count % 2 == 1:
			if odd is False:
				odd = True
			else:
				return False

	return True


