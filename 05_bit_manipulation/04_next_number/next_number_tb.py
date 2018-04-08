"""
Brute force solution for first ~32'ish values.
"""


from next_number import *
# from next_number_sol1 import *


bin_ones_count = {}
low = 1
high = 32
pad_len = 5


# Populate dictionary for the range
for i in range(low, high):
    # target number
    bin_arr = convert_to_binary(i)
    num_of_ones = bin_arr.count(1)

    # format the binary number in order to search the dictionary
    bin_str = ''.join(str(x) for x in bin_arr)
    bin_str = bin_str.zfill(pad_len)

    try:
        bin_ones_count[num_of_ones].append(bin_str)
    except:
        bin_ones_count[num_of_ones] = [bin_str]


# Print the contents of the bin_ones_count dictionary
for k, v in bin_ones_count.items():
    print('number of ones: {0}'.format(k))
    print(v)
print()


# Testing
for i in range(low, high):
    # target number
    bin_arr = convert_to_binary(i)
    num_of_ones = bin_arr.count(1)

    # format the binary number in order to search the dictionary
    bin_str = ''.join(str(x) for x in bin_arr)
    bin_str = bin_str.zfill(pad_len)

    # this list contains the target number and the next smaller/larger number
    # with the same number of ones in its binary representation
    ones_array = bin_ones_count[num_of_ones]
    ones_array_len = len(ones_array)
    one_index = ones_array.index(bin_str)


    print('\tinput: {0} \t\tbinary: {1} \t\t# of ones: {2}'.format(i, bin_str, num_of_ones))
    print('smaller:', end=' ')
    if (one_index - 1) < 0:
        print('None')
    else:
        print(ones_array[one_index - 1])

    print('larger:', end=' ')
    if (one_index + 1) >= ones_array_len:
        print('None')
    else:
        print(ones_array[one_index + 1])




# check for what happens with 10 (2)



