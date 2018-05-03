# Solution


def draw_line(screen, width, x1, x2, y):
    start_offset = x1 % 8
    first_full_byte = x1 // 8
    if (start_offset != 0):
        first_full_byte += 1

    end_offset = x2 % 8
    last_full_byte = x2 // 8
    if (end_offset != 7):
        last_full_byte -= 1


    # Set full bytes.
    for b in range(first_full_byte, last_full_byte + 1):
        screen[(width // 8) * y + b] = 0xFF  # cast result to byte


    # Create masks for start and end of line.
    start_mask = (0xFF >> start_offset)  # cast result to byte
    end_mask = ~(0xFF >> (end_offset + 1))  # cast result to byte


    # Set start and end of line.
    if ((x1 // 8) == (x2 // 8)):
        # x1 and x2 are in the same byte.
        mask = start_mask & end_mask  # cast result to byte
        screen[(width // 8) * y + (x1 // 8)] = (screen[(width // 8) * y + (x1 // 8)]) | mask
    else:
        if (start_offset != 0):
            byte_number = (width // 8) * y + first_full_byte - 1
            screen[byte_number] = screen[byte_number] | start_mask
        if (end_offset != 7):
            byte_number = (width // 8) * y + last_full_byte + 1
            screen[byte_number] = screen[byte_number] | end_mask


