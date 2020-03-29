# Testing file size after rewriting a file.

from file_system import *


dir_1 = Directory("dir_1", None)
file_1 = File("file_1", dir_1)
file_2 = File("file_2", dir_1)


print('New:')
print(dir_1.get_full_path())
print(file_1.get_full_path())
print(file_2.get_full_path())
print()


print('Contents of dir_1:')
dir_1.get_contents()
print()



print('Size of dir_1:')
print(dir_1.get_size())
print()



print('Writing to files:')
file_1.set_content('Day 1 of quarantine:')
file_2.set_content('Running out of ideas')



