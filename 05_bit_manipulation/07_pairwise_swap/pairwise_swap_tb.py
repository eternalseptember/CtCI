# from pairwise_swap import *
from pairwise_swap_sol import *


def print_binary(num1, num2):
	bin1 = bin(num1)[2:]
	bin2 = bin(num2)[2:]
	print('{0} <--> {1}'.format(bin1, bin2))


# Testing
# Test case 1: 101010 <-> 010101
num = 42
results = pairwise_swap(num)
print_binary(num, results)


# Test case 2: 111 or 0111 <-> 1011
num = 7
results = pairwise_swap(num)
print_binary(num, results)


# Test case 3: 10001 <-> 100010
num = 17
results = pairwise_swap(num)
print_binary(num, results)


