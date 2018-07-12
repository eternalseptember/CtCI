from jukebox import *


jukebox = Jukebox()

jukebox.add_song('test song 1')
print(jukebox)


# play song without adding money
result = jukebox.play_song(1)
print(result)


