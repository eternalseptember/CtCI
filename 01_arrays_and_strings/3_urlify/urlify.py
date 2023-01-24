"""
Write a method to replace all spaces in a string with '%20'. You may assume
that the string has sufficient space at the end to hold the additional
characters, and that you are given the "true" length of the string.
"""

def urlify(str):
	return str.replace(' ', '%20')


# Testing
inp = 'Mr John Smith'
print(urlify(inp))
