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

    # Set full bytes
    for b in range(first_full_byte, last_full_byte + 1):
        # screen[(width // 8) * y + b] = (byte) 0xFF
        screen[(width // 8) * y + b] = 0xFF

    # Create masks for start and end of line
    # start_mask = (byte) (0xFF >> start_offset)
    start_mask = (0xFF >> start_offset)
    # end_mask = (byte) ~(0xFF >> (end_offset + 1))
    end_mask = ~(0xFF >> (end_offset + 1))

    # Set start and end of line


