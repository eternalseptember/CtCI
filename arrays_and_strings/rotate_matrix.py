"""
Given an image represented by an NxN matrix, where each pixel in
the image is 4 bytes, write a method to rotate the image by 90
degrees. Can you do this in place?
"""


def rotate(N, image):
	print(image)



N = 6

image = []
starting_num = 0

# fill in numbers as the image
for row in range(N):
	new_col = []
	for col in range(N):
		new_col.append(starting_num)
		starting_num += 1
	image.append(new_col)



rotate(N, image)



