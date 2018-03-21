# The solution provided.


"""
def string_to_binary(num):
    if (num >= 1) or (num <= 0):
        return "Error. Range is 0 < number < 1."

    binary_str = '.'

    while num > 0:
        # setting a limit on length: 32 characters
        if len(binary_str) >= 32:
            return "Error. Cannot be represented accurately with at most 32 chars."

        r = num * 2

        if (r >= 1):
            binary_str += '1'
            num = r - 1
        else:
            binary_str += '0'
            num = r

        # print('binary str: {0}'.format(binary_str))

    return binary_str
"""


def string_to_binary(num):
    if (num >= 1) or (num <= 0):
        return "Error. Range is 0 < number < 1."

    binary_str = '.'
    frac = 0.5

    while num > 0:
        # setting a limit on length: 32 characters
        if len(binary_str) >= 32:
            return "Error. Cannot be represented accurately with at most 32 chars."

        if (num >= frac):
            binary_str += '1'
            num -= frac
        else:
            binary_str += '0'

        frac /= 2

        # print('binary str: {0}'.format(binary_str))

    return binary_str




