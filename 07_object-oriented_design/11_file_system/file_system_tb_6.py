# Testing the effects of renaming files and folders.
# How does it total sizes of nested folder structure?

from file_system import *


# dir_1 has 2 files and 2 folders.
dir_1 = Directory("dir_1", None)
file_1 = File("file_1", dir_1)
file_2 = File("file_2", dir_1)
# dir_2 has three files?
dir_2 = Directory("dir_2", dir_1)
file_3 = File("file_3", dir_2)
file_4 = File("file_4", dir_2)
file_5 = File("file_5", dir_2)
# dir_4 has four files?
dir_3 = Directory("dir_3", dir_1)
file_6 = File("file_6", dir_3)
file_7 = File("file_7", dir_3)
file_8 = File("file_8", dir_3)
file_9 = File("file_9", dir_3)


print('Number of items in dir_1:')
print(dir_1.get_num_of_items())
print()



print('How big is dir_1 so far?')
print(dir_1.get_size())
print()



print("What is inside dir_1?")
dir_1.get_contents()
print()



print("Rename a file.")
file_1.rename("new file")
print()



print("What is inside dir_1?")
dir_1.get_contents()
print()



print("Get full paths:")
print(dir_1.get_full_path())
print(file_1.get_full_path())








