from jukebox import *


jukebox = Jukebox()

jukebox.add_song('test song 1')
jukebox.add_song('test song 2')
print(jukebox)


# play song without adding money
result = jukebox.play_song(1)
print(result)

# play song after inserting insufficient money
jukebox.insert_money(50)
result = jukebox.play_song(1)
print(result)

# play song after inserting enough money
jukebox.insert_money(75)
result = jukebox.play_song(1)
print(result)

