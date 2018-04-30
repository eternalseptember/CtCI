# Solution


def draw_screen(screen, width, x1, x2, y):
    start_offset = x1 % 8
    first_full_byte = x1 // 8

    if (start_offset != 0):
        first_full_byte += 1

    end_offset = x2 % 8
    last_full_byte = x2 // 8

    if (end_offset != 7):
        last_full_byte -= 1


