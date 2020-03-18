# Testing folder size

from file_system import *


dir_1 = Directory("dir_1", None)

file_1 = File("file_1", dir_1)
file_2 = File("file_2", dir_1)

dir_1.get_contents()


print('Size of dir_1:')
print(dir_1.get_size())


print('Writing to files:')
file_1.set_content('hello world!')
file_2.set_content('my name is __.')




"""
print(type(dir_1))
print(type(file_1))
"""


