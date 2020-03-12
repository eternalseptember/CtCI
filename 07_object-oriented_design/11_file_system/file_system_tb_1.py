# Testing rename

from file_system import *


def print_info(item, new_name=None):
    print('Name:', end=' ')
    print(item)

    if new_name is not None:
        item.rename(new_name)
        print('New name:', end=' ')
        print(item)
    print()


print('\t\tEntry functions')
entry_1 = Entry("entry_1", None)
print_info(entry_1, "test_entry_1")

print('\t\tFile functions')
file_1 = File("file_1", None)
print_info(file_1, "test_file_1")

print('\t\tDirectory functions')
dir_1 = Directory("dir_1", None)
print_info(dir_1, "test_dir_1")




