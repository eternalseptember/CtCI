"""
Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a
double, print the binary representation. If the number cannot be
represented accurately in binary with at most 32 characters, print "ERROR".
"""


def string_to_binary(num):
    dec_places = 0
    dec_point_found = False
    dec_num = ''

    # gets the number of decimal places and
    # the number to convert to binary
    for char in str(num):
        if char == '.':
            dec_point_found = True
        elif dec_point_found:
            dec_num += char
            dec_places += 1

    # converts the number after the decimal point to binary
    bin_result = []
    div_result = int(dec_num)

    while (div_result > 0):
        # The result should not be returned.
        if len(bin_result) >= 32:
            return 'ERROR'

        rem = div_result % 2
        div_result = div_result // 2
        bin_result.insert(0, rem)


    bin_string = ''.join(str(x) for x in bin_result)
    return bin_string







