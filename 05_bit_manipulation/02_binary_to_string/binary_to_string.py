"""
Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a
double, print the binary representation. If the number cannot be
represented accurately in binary with at most 32 characters, print "ERROR".
"""


def string_to_binary(num):
	if (num >= 1) or (num <= 0):
		return "ERROR. Range is 0 < number < 1."

	bin_result = '.'

	while (num > 0):
		# The result should not be returned.
		if len(bin_result) >= 32:
			return 'ERROR. Cannot be represented accurately with at most 32 chars.'

		mult_result = num * 2

		if (mult_result >= 1):
			bin_result += '1'
			num = mult_result - 1
		else:
			bin_result += '0'
			num = mult_result


	return bin_result







