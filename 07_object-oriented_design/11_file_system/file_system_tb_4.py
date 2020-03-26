# Testing folder size after deleting file.

from file_system import *


dir_1 = Directory("dir_1", None)
file_1 = File("file_1", dir_1)
file_2 = File("file_2", dir_1)
file_3 = File("file_3", dir_1)
file_4 = File("file_4", dir_1)


print('New:')
print(dir_1.get_full_path())
print(file_1.get_full_path())
print(file_2.get_full_path())
print(file_3.get_full_path())
print(file_4.get_full_path())
print()



print('Contents of dir_1:')
dir_1.get_contents()
print()



print('Size of dir_1:')
print(dir_1.get_size())
print()



print('Writing to files:')
file_1.set_content('Do not go gentle into that good night,')
file_2.set_content('Old age should burn and rave at close of day;')
file_3.set_content('Rage, rage against the dying of the light.')
file_4.set_content('Though wise men at their end know dark is right,')

print(file_1.get_content())
print(file_2.get_content())
print(file_3.get_content())
print(file_4.get_content())
print()



print('File sizes:')
print(file_1.get_size())
print(file_2.get_size())
print(file_3.get_size())
print(file_4.get_size())

print('Folder size:')
print(dir_1.get_size())








