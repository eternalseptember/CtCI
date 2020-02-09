from file_system import *


def print_info(item, new_name=None):
    print(item)
    print()
    if new_name is not None:
        item.rename(new_name)
        print(item)
        print()	



print('Entry functions.')
entry_1 = Entry("entry_1", None)
print_info(entry_1)

print('File functions.')
file_1 = File("file_1", None, 32)
print_info(file_1)

print('Directory functions.')
dir_1 = Directory("dir_1", None)
print_info(dir_1)


