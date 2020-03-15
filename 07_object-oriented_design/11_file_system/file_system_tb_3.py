# Testing basic file functions

from file_system import *


dir_1 = Directory("dir_1", None)

file_1 = File("file_1", dir_1)
file_2 = File("file_1", dir_1)
# test duplicate file names?

dir_1.get_contents()


"""
print(type(dir_1))
print(type(file_1))
"""


