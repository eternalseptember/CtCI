# Testing folder size

from file_system import *


dir_1 = Directory("dir_1", None)
file_1 = File("file_1", dir_1)
file_2 = File("file_2", dir_1)

print('Contents of dir_1:')
dir_1.get_contents()
print()


print('Size of dir_1:')
print(dir_1.get_size())
print()


print('Writing to files:')
file_1.set_content('hello world!')
file_2.set_content('my name is __.')
print(file_1.get_content())
print(file_2.get_content())
print()


print('Size of file_1:')
print(file_1.get_size())
print('Size of file_2:')
print(file_2.get_size())
print('Total size of dir_1:')
print(dir_1.get_size())



"""
print(type(dir_1))
print(type(file_1))
"""


