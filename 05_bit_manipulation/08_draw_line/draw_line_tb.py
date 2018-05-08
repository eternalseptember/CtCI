# from draw_line import *
from draw_line_sol import *


# Test: Drawing blank screen
# screen = [0, 0, 0, 0]
# draw_screen(screen)

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


# Trying to get a longer line
# width: 16; height: 8
screen = [0, 0, 0, 0, 0, 0, 0, 0]
width = 16  # can be larger than the number of entries in the screen
x1 = 10
x2 = 14
y = 7  # 7 is the max limit because row split
draw_line(screen, width, x1, x2, y)
print(screen)
draw_screen(screen)




