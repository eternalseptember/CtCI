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
print(file_2.get_full_path())
print(dir_2.get_full_path())
print(file_3.get_full_path())
print(file_4.get_full_path())
print(file_5.get_full_path())
print(dir_3.get_full_path())
print(file_6.get_full_path())
print(file_7.get_full_path())
print(file_8.get_full_path())
print(file_9.get_full_path())
print()



print('Write into all the files and calculate dir_1 file size.')
file_1.set_content('What would you like?')
file_2.set_content('What is it?')
file_3.set_content('Have some wine!')
file_4.set_content('The thunderstorm came with hail.')
file_5.set_content('Pancakes, please.')
file_6.set_content('If you could live anywhere, where would you live and why?')
file_7.set_content('Want some?')
file_8.set_content('I want a rainbow unicorn.')
file_9.set_content('The lemonade was too sour.')

print('File sizes:')
print(file_1.get_size())
print(file_2.get_size())
print(file_3.get_size())
print(file_4.get_size())
print(file_5.get_size())
print(file_6.get_size())
print(file_7.get_size())
print(file_8.get_size())
print(file_9.get_size())
print()

print('dir_2 total size:')
print(dir_2.get_size())

print('dir_3 total size:')
print(dir_3.get_size())

print('dir_1 total size:')
print(dir_1.get_size())

print()



# one more level of nested folders
dir_4 = Directory("dir_4", dir_3)
file_10 = File("file_10", dir_4)
file_11 = File("file_11", dir_4)
file_12 = File("file_12", dir_4)



print("What is inside dir_1?")
dir_1.get_contents()
print()

print("What is inside dir_3")
dir_3.get_contents()
print()











