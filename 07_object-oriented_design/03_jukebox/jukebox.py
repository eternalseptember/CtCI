"""
Design a musical jukebox using object-oriented principles.
"""


class Jukebox():
    def __init__(self):
        self.music_list = []


    def add_song(self, song):
        if song not in self.music_list:
            self.music_list.append(song)


