"""
Given a string, write a function to check if it is a permutation
of a palindrome. A palindrome is a word or phrase that is the same
forwards and backwards. A permutation is a rearrangement of
letters. The palindrome dos nto need to be limited to just
dictionary words.
"""


from collections import Counter


def check_palindrome(str):
	str = str.lower().replace(' ', '')
	list_of_letters = Counter(str)

	str_len = len(str)
	if str_len % 2 == 0:
		for num in list_of_letters.values():
			if num % 2 == 0:
				return True
			else:
				return False
	else:
		odd = 0
		for num in list_of_letters.values():
			if num % 2 == 1:
				odd += 1

		if odd == 1:
			return True
		else:
			return False



inp = 'Tact Coa'
permutations = check_palindrome(inp)
print(permutations)


