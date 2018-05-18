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
    height = len(screen) * 8 // width

    # adjusts the screen


def draw_screen(screen, width):
    height = len(screen) * 8 // width
    columns = width // 8
    screen_index = 0

    for row in range(height):

        for column in range(columns):
            pixel_group = screen[screen_index]

            # Convert pixel to bit representation.
            pixels = bin(pixel_group)[2:].zfill(8)

            # Print line.
            for pixel in pixels:
                if pixel == '0':
                    print('_', end='')
                elif pixel == '1':
                    print('x', end='')

            screen_index += 1

        print()



