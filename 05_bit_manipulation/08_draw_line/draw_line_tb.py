# from draw_line import *
from draw_line_sol import *


"""
# 'xxxx' on second line from top
screen = [0, 0, 0, 0]
width = 8
x1 = 2
x2 = 5
y = 1
draw_line(screen, width, x1, x2, y)
draw_screen(screen)


# 'xxxx' on last line
screen = [0, 0, 0, 0, 0, 0, 0, 0]
width = 8
x1 = 2
x2 = 5
y = 7
draw_line(screen, width, x1, x2, y)
draw_screen(screen)


# 'xxxxxxxx' on first line
screen = [0, 0, 0, 0, 0, 0, 0, 0]
width = 8
x1 = 0
x2 = 7
y = 0
draw_line(screen, width, x1, x2, y)
draw_screen(screen)
"""


# Trying to get a longer line.
# Each byte is 8 consecutive pixels.
# Two consecutive bytes make up a line on the screen.
# Screen's width is 16.
# Screen's height is 8.

screen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
width = 16  # Can be larger than the number of entries in the screen?
x1 = 0
x2 = 15 # Theoretically, this is one full line.
y = 7  # Width is numbered 0 to 7. 7 is the last line.
draw_line(screen, width, x1, x2, y)
draw_screen(screen)




