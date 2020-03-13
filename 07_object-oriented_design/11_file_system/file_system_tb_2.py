# Testing basic file functions

from file_system import *


dir_1 = Directory("dir_1", None)

file_1 = File("file_1", dir_1)
print(file_1.get_size())
file_1.set_content('stuff in file_1')
print(file_1.get_size())



