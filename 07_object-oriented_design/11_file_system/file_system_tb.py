from file_system import *


def print_info(item, new_name=None):
    print(item)
    print()
    if new_name is not None:
        item.rename(new_name)
        print(item)
        print()	



print('\t\tEntry functions.')
entry_1 = Entry("entry_1", None)
print_info(entry_1)
# print_info(entry_1, "test_entry_1")

print('\t\tFile functions.')
file_1 = File("file_1", None, 32)
print_info(file_1)
# print_info(file_1, "test_file_1")

print('\t\tDirectory functions.')
dir_1 = Directory("dir_1", None)
print_info(dir_1)
# print_info(dir_1, "test_dir_1")

print('Contents of dir_1:')
dir_1.get_contents()
print('\tdir_2 is nested inside dir_1.')
dir_2 = Directory("dir_2", dir_1)
print('Contents of dir_1:')
dir_1.get_contents()

