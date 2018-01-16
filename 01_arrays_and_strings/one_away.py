"""
There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one
edit (or zero edits) away.
"""


def one_away(str1, str2):
    """
    Takes O(N) time, where n is the length of the shorter string.
    """
    str1_len = len(str1)
    str2_len = len(str2)

    if str1_len == str2_len:
        return check_replace(str1, str2)
    elif (str2_len - str1_len) == 1:
        return check_insert_or_remove(str1, str2)
    elif (str1_len - str2_len) == 1:
        return check_insert_or_remove(str2, str1)
    else:
        return False


def check_replace(str1, str2):
    # only one character should be changed
    found_diff = False
    str_len = len(str1)

    for index in range(str_len):
        if str1[index] != str2[index]:
            if found_diff is True:
                return False
            else:
                found_diff = True

    return True


def check_insert_or_remove(str1, str2):
    # return True if str2 inserted a character
    diff = 0
    str2_len = len(str2)
    str1_index = 0

    for str2_index in range(str2_len):
        if (str1_index + 1) == str2_len:
            # str1_index would be out of bounds
            # checks if the insertion happened at the end
            diff += 1
        elif str1[str1_index] == str2[str2_index]:
            str1_index += 1
        else:
            diff += 1

    if diff == 1:
        return True
    else:
        return False


# Testing
# true, true, true, false, true, false
str_1_set = ['pale', 'pales', 'pale', 'pale', 'pale', 'app']
str_2_set = ['ple', 'pale', 'bale', 'bake', 'pales', 'apples']

sets = len(str_1_set)
for i in range(sets):
    str_1 = str_1_set[i]
    str_2 = str_2_set[i]

    result = one_away(str_1, str_2)
    print(result)


