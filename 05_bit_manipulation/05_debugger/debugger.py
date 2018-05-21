"""
Explain what the following code does:
n & (n-1) == 0
"""

"""
Solution:

What does it mean if A & B == 0?
n and (n-1) never share a 1 bit in the same place.

Example:
n   = abcde1000
n-1 = abcde0001

If n and (n-1) must have no 1's in common, then abcde must be all 0's.
n must look like this: 00001000.
Therefore, n is a power of 2.

n & (n-1) checks if n is a power of 2 (or if n is 0).
"""



# Testing
test_arr = [i for i in range(300)]

for num in test_arr:
    result = num & (num-1)

    if result == 0:
        print(num)



