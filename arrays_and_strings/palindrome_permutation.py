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
	print(str_len)


	return list_of_letters



inp = 'Tact Coa'
permutations = check_palindrome(inp)
print(permutations)


