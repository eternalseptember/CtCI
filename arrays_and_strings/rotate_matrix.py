"""
Given an image represented by an NxN matrix, where each pixel in
the image is 4 bytes, write a method to rotate the image by 90
degrees. Can you do this in place?
"""

"""
def rotate(N, image):
	new_image = []
	for col in range(N):
		col_entry = []
		for row in range(N):
			col_entry.append(image[row][col])
		new_image.append(col_entry[::-1])

	print('Original image:')
	print(image)
	print('Rotated image:')
	print(new_image)
"""


def rotate(image):
	# O(N^2) time.
	N = len(image)

	# Returns False if the image doesn't exist or isn't a square.
	if ((N == 0) or (N != len(image[0]))):
		return False

	# rotate layers


# Testing
N = 4
image = []
starting_num = 1

# fill in numbers as the image
for row in range(N):
	new_col = []
	for col in range(N):
		new_col.append(starting_num)
		starting_num += 1
	image.append(new_col)

# rotate(N, image)

rotate(image)

