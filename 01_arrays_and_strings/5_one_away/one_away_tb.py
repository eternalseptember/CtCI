# Test case for "one away" problem.


from one_away import *


# true, true, true, false, true, false
str_1_set = ['pale', 'pales', 'pale', 'pale', 'pale', 'app']
str_2_set = ['ple', 'pale', 'bale', 'bake', 'pales', 'apples']

sets = len(str_1_set)
for i in range(sets):
    str_1 = str_1_set[i]
    str_2 = str_2_set[i]

    result = one_away(str_1, str_2)
    print(result)


