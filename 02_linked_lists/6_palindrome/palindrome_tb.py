# Test cases for the "palindrome" problem.


from palindrome import *


# Expected results: True, True, True, True, False, False
test_cases = ['racecar', 'mom', 'noon', 'toot', 'cat', 'plop']

for case in test_cases:
    test_palindrome_function(case)

