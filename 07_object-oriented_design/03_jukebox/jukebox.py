"""
Design a musical jukebox using object-oriented principles.
"""


class Coin():
    def __init__(self, value):
        self.value = value


class Jukebox():
    def __init__(self):
        self.song_id = 0
        self.music_menu = {}  # music_menu[song_id] = 'song name'
        self.play_count = {}  # play_count[song_id] = times_played
        self.coin_inserted = {}
        self.money_collected = 0


    def add_song(self, song):
        if song not in self.music_menu:
            self.music_menu[self.song_id] = song
            self.play_count[self.song_id] = 0
            self.song_id += 1


