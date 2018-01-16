"""
Given two strings, write a method to decide if one
is a permutation of the other.
"""


def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    first_str = list(str1)

    # case-sensitive, whitespace is significant
    for char in str2:
        try:
            first_str.remove(char)
        except ValueError:
            return False

    return True




