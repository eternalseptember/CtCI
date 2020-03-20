# Testing basic file functions.

from file_system import *


dir_1 = Directory("dir_1", None)
file_1 = File("file_1", dir_1)



print('New:')
print(dir_1.get_full_path())
print(file_1.get_full_path())
print()



print('File size before writing to file:')
print(file_1.get_size())
print()



print('Writing to file:')
file_1.set_content('file_1 says \'hello world!\'')
print(file_1.get_content())
print()



print('File size after writing to file:')
print(file_1.get_size())
print()


