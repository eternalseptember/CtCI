# from draw_line import *
from draw_line_sol import *


# Each byte is 8 consecutive pixels.
# Two consecutive bytes make up a line on the screen.
# Screen's width is 16.
# Screen's height is 8.

# Each line on the screen has a height of four.
screen = [0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0]
width = 16
x1 = 0
x2 = 15  # One full line.
y = 7  # Height is numbered 0 to 7. 7 is the last line.
draw_line(screen, width, x1, x2, y)
draw_screen(screen, width)


# Three consecutive bytes make up a line on the screen.
# Screen's width is 24.
# Screen's height is 8.

# Each line on the screen has height of two.
screen = [0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0]
width = 24
x1 = 7
x2 = 16  # There will be a "full byte", and an extra pixel on each side.
y = 6  # Second-to-last line.
draw_line(screen, width, x1, x2, y)
draw_screen(screen, width)





