from jukebox import *


jukebox = Jukebox()

jukebox.add_song('test song 1')
jukebox.add_song('test song 2')
jukebox.add_song('test song 3')
jukebox.add_song('test song 4')
jukebox.add_song('test song 5')


# play song without adding money
result = jukebox.play_song(1)
print(result)

# play song 1 time
jukebox.insert_money(10)
result = jukebox.play_song(2)
print(result)

# play song 3 times
jukebox.insert_money(25)
result = jukebox.play_song(3)
print(result)

# play song 7 times
jukebox.insert_money(50)
result = jukebox.play_song(4)
print(result)


# print jukebox info
print()
print(jukebox)


