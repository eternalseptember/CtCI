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

    return new_image
"""


def rotate(N, image):
    # O(N^2) time.

    # Returns False if the image doesn't exist or isn't a square.
    if ((N == 0) or (N != len(image[0]))):
        return False

    # rotate layers
    # what kind of division?
    for layer in range(N // 2):
        first = layer
        last = N - 1 - layer

        for i in range(first, last):
            offset = i - first
            top = image[first][i]  # save top

            # left -> top
            image[first][i] = image[last-offset][first]

            # bottom -> left
            image[last-offset][first] = image[last][last-offset]

            # right -> bottom
            image[last][last - offset] = image[i][last]

            # top -> right
            image[i][last] = top  # right <- saved top

    return True



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

# for testing the first function
# new_image = rotate(N, image)
# print(new_image)

# for testing the answer
rotate(N, image)
print(image)


