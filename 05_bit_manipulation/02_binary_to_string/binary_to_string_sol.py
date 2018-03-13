# The solution provided.


def string_to_binary(num):
    if (num >= 1) or (num <= 0):
        return "Error"


    binary_str = '.'

    while num > 0:
        # setting a limit on length: 32 characters
        if len(binary_str) >= 32:
            return "Error"



    return None


