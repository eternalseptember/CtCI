# The solution provided.


def string_to_binary(num):
    if (num >= 1) or (num <= 0):
        return "Error 1"


    binary_str = '.'

    while num > 0:
        print(len(binary_str))

        # setting a limit on length: 32 characters
        if len(binary_str) >= 32:
            return "Error 2"

        r = num * 2
        print('r: {0}'.format(r))

        if (r >= 1):
            binary_str += '1'
            num = r - 1
        else:
            binary_str += '0'
            num = r

        print('binary str: {0}'.format(binary_str))
        print('num: {0}'.format(num))

        print()


    return binary_str


