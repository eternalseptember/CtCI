# Test cases for "rotate matrix" problem.


from rotate_matrix import *


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



