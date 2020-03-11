from file_system import *


dir_1 = Directory("dir_1", None)
print('\t\tContents of dir_1 before adding a folder:')
dir_1.get_contents()
print()
# print('\tSize of dir_1:')
# print(dir_1.get_size())


print('\t\tdir_2 is nested inside dir_1.')
dir_2 = Directory("dir_2", dir_1)
print(dir_2.get_full_path())
print()

print('\t\tContents of dir_1 after adding a folder:')
dir_1.get_contents()
print()

print('\t\tThree folders deep.')
dir_3 = Directory("dir_3", dir_2)
print(dir_3.get_full_path())
print()


# Renaming different folder levels
print('\t\tRenaming dir_1.')
dir_1.rename('dir_1_new')
print(dir_3.get_full_path())
print('\t\tContents of dir_1_new:')
dir_1.get_contents()
print('\t\tRenaming dir_2.')
dir_2.rename('dir_2_new')
print(dir_3.get_full_path())
print('\t\tContents of dir_1_new:')
dir_1.get_contents()
print()

# Adding files
print('\t\tPut files inside dir_1.')
file_1 = File("file_1", dir_1)
print(file_1.get_full_path())
# write to these files!
file_2 = File("file_2", dir_1)
print(file_2.get_full_path())
file_3 = File("file_3", dir_1)
print(file_3.get_full_path())

print('\t\tContents of dir_1_new:')
dir_1.get_contents()
print()
print('\tNumber of items in dir_1:')
print(dir_1.get_num_of_items())
print('\tRenaming file_1.')
file_1.rename('file_1_new')
print('\tWriting to file_1:')
file_1.set_content('test test test')
print('\tSize of file_1:')
print(file_1.get_size())
print(file_1.get_content())
print('\tDeleting file_1:')
dir_1.delete_entry(file_1)
dir_1.get_contents()
print('\tNumber of items in dir_1:')
print(dir_1.get_num_of_items())
print('\tSize of dir_1:')
print(dir_1.get_size())






