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

    while ((div_result > 0) and (len(bin_result) < 32)):
        rem = div_result % 2
        div_result = div_result // 2
        bin_result.insert(0, rem)

    # ??? shift the binary???


    # checks to see if result should be returned
    if (div_result == 0) or (len(bin_result) <= 32):
        bin_string = ''.join(str(x) for x in bin_result)
        return bin_string
    else:
        return 'ERROR'



def binary_to_int(bin_str):
    bin_list = []
    int_total = 0
    bit_pos = 0

    for bit in list(bin_str):
        bin_list.append(int(bit))

    while len(bin_list) > 0:
        current_bit = bin_list.pop()
        int_total += (current_bit * 2**bit_pos)
        bit_pos += 1

    return int_total





