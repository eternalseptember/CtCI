# The solution provided.


def string_to_binary(num):
    if (num >= 1) or (num <= 0):
        return "Error"


    binary_str = '.'

    while num > 0:
        # setting a limit on length: 32 characters
        if len(binary_str) >= 32:
            return "Error"

        r = num * 2
        if (r >= 1):
            binary_str += '1'
            num = r - 1
        else:
            binary_str += '0'
            num = r


    return binary_str


