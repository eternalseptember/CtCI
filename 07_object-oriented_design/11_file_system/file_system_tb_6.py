# Testing the effects of renaming files and folders.

from file_system import *


dir_1 = Directory("dir_1", None)
file_1 = File("file_1", dir_1)
file_2 = File("file_2", dir_1)
dir_2 = Directory("dir_2", dir_1)
dir_3 = Directory("dir_3", dir_1)


# How many items are in dir_1?
print('Number of items in dir_1:')
print(dir_1.get_num_of_items())


