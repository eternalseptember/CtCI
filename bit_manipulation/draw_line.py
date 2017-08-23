"""
A monochrome screen is stored as a single array of bytes, allowing eight
consecutive pixels to be stored in one byte. The screen has width w,
where w is divisible by 8 (that is, no byte will be split across rows).
The height of the screen, of course, can be derived from the length of
the array and the width. Implement a function that draws a horizontal
line from (xl, y) to (x2, y).

The method signature should look something like:
drawLine(byte[] screen, int width, int xl, int x2, int y)
"""


def draw_line(screen, width, x1, x2, y):
	# length and height are synonomous in this problem
	height = len(screen)
	
	return None


def draw_screen(screen):
	for row in screen:
		row_binary = int_to_binary(row)

		# pad the binary representation for 8 bits long
		while len(row_binary) < 8:
			row_binary.insert(0, 0)

		# print the row
		for pixel in row_binary:
			if pixel == 0:
				print('_', end='')
			else:
				print('x', end=' ')
		print()


def int_to_binary(num):
	bin_digits = []
	quotient = num

	while quotient > 0:
		rem = quotient % 2
		quotient = quotient // 2
		bin_digits.insert(0, rem)

	return bin_digits


# Testing
# blank screen
screen = [0, 0, 0, 0]
draw_screen(screen)


# _ is a blank placeholder; represents 0
"""
________ : 0
__xxxx__ : 
________ : 0
________ : 0
"""






