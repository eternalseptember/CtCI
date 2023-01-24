# Solution


def draw_line(screen, width, x1, x2, y):
	# Draw a horizontal line from (xl, y) to (x2, y).
	first_full_byte = x1 // 8
	start_offset = x1 % 8
	if (start_offset != 0):
		first_full_byte += 1

	last_full_byte = x2 // 8
	end_offset = x2 % 8
	if (end_offset != 7):
		last_full_byte -= 1


	# Set full bytes.
	for b in range(first_full_byte, last_full_byte + 1):
		screen[(width // 8) * y + b] = 0xFF


	# Create masks for start and end of line.
	start_mask = (0xFF >> start_offset)
	end_mask = ~(0xFF >> (end_offset + 1))


	# Set start and end of line.
	if ((x1 // 8) == (x2 // 8)):
		# x1 and x2 are in the same byte.
		mask = start_mask & end_mask
		screen[(width // 8) * y + (x1 // 8)] = (screen[(width // 8) * y + (x1 // 8)]) | mask
	else:
		if (start_offset != 0):
			byte_number = (width // 8) * y + first_full_byte - 1
			screen[byte_number] = screen[byte_number] | start_mask
		if (end_offset != 7):
			byte_number = (width // 8) * y + last_full_byte + 1
			screen[byte_number] = screen[byte_number] | end_mask


# This is not part of the solution, but is here for testing purposes.
def print_screen(screen, width):
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

	print()


