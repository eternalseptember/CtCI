# from draw_line import *
from draw_line_sol import *


# Test: Drawing blank screen
# screen = [0, 0, 0, 0]
# draw_screen(screen)


# Initial test
"""
________
__xxxx__
________
________
"""
"""
screen = [0, 0, 0, 0]
width = 8
x1 = 2
x2 = 5
y = 1
draw_line(screen, width, x1, x2, y)
# print(screen)
draw_screen(screen)
"""



# Testing the problem
screen = [0, 0, 0, 0, 0, 0, 0, 0]
width = 8
x1 = 2
x2 = 5
y = 7
draw_line(screen, width, x1, x2, y)
# print(screen)
draw_screen(screen)






