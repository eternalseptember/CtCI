# Test case for "palindrome permutation" problem


from palindrome_permutation import *


# Testing
# True, True, True, True, False
inp = ['Tact Coa', 'atco cta', 'tactcoapapa', 'llggo', 'logo']

for phrase in inp:
	permutations = check_palindrome(phrase)
	print(permutations)


