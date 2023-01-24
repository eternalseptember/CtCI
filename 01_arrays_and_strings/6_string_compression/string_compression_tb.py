# Test cases for "string compression" problem.


from string_compression import *


# Expected answer: a2b1c5a3, abcde
inp = ['aabcccccaaa', 'abcde']

for string in inp:
	print(compress(string))

