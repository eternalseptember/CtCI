from draw_line import *
# from draw_line_sol import *


# Each byte is 8 consecutive pixels.
# 0 (no line) <= pixel_group <= 255 (8 pixel line)
# 0 <= y <= height.

# *****************************************************************************


# Screen's width is 8.
# Screen's height is 8.
# A line across the screen is 1 byte.
# Each line of the array has a screen height of 8.
screen = [0, 0, 0, 0, 0, 0, 0, 0]
width = 8

# Draw a diagonal line: \
for i in range(8):
	x1 = i
	x2 = i  # 1 pixel line
	y = i
	draw_line(screen, width, x1, x2, y)

print_screen(screen, width)

# Draw another diagonal line: /
for i in range(7, -1, -1):
	x1 = i
	x2 = i  # 1 pixel line
	y = 7 - i
	draw_line(screen, width, x1, x2, y)

print_screen(screen, width)


# *****************************************************************************


# Screen's width is 16.
# Screen's height is 8.
# A line across the screen is 2 consecutive bytes.
# Each line of the array has a screen height of 4.
screen = [0, 0, 0, 0, 0, 0, 0, 0,
		  0, 0, 0, 0, 0, 0, 0, 0]
width = 16

# Line 1
x1 = 0
x2 = 7  # Full byte on the first half.
y = 0  # 0 is the first line.
draw_line(screen, width, x1, x2, y)

# Line 2
x1 = 8
x2 = 15  # Full byte on the second half.
y = 1  # 1 is the second line.
draw_line(screen, width, x1, x2, y)

# Line 3
x1 = 0
x2 = 15  # Full line across.
y = 7  # 7 is the last line.
draw_line(screen, width, x1, x2, y)

print_screen(screen, width)


# *****************************************************************************


# Screen's width is 24.
# Screen's height is 8.
# A line across the screen is 3 consecutive bytes.
# Each line of the array has a screen height of 2.
screen = [0, 0, 0, 0, 0, 0,
		  0, 0, 0, 0, 0, 0,
		  0, 0, 0, 0, 0, 0,
		  0, 0, 0, 0, 0, 0]
width = 24

# Line 1
x1 = 9
x2 = 14  # Line segment in the middle.
y = 2
draw_line(screen, width, x1, x2, y)

# Line 2
x1 = 8
x2 = 15  # Full byte line in the middle.
y = 3
draw_line(screen, width, x1, x2, y)

# Line 3
x1 = 7
x2 = 16  # Full byte in the middle and an extra pixel on each side.
y = 4
draw_line(screen, width, x1, x2, y)

print_screen(screen, width)


# *****************************************************************************


# Screen's width is 48.
# Screen's height is 16.
# A line across the screen is 6 consecutive bytes.
# Each line of the array has a screen height of 2.
screen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
width = 48

"""
# Line 1
x1 = 0
x2 = 0
y = 0
draw_line(screen, width, x1, x2, y)
"""

print_screen(screen, width)



