"""
Design a musical jukebox using object-oriented principles.
"""


class Jukebox():
    def __init__(self):
        self.song_id = 0
        self.music_menu = {}  # music_menu[song_id] = 'song name'
        self.play_count = {}  # play_count[song_id] = times_played
        self.money_inserted = 0  # unit in cents
        self.total_collected = 0
        self.price = 75  # price per song, for testing purpose


    def __str__(self):
        jukebox_info = 'Money collected in cents: {0}\n'\
            .format(self.total_collected)

        # tally of each song played
        for song in self.play_count.keys():
            jukebox_info += '{0} played {1} times.\n'\
                .format(song, self.play_count[song])

        return jukebox_info


    def add_song(self, song):
        if song not in self.music_menu:
            self.music_menu[self.song_id] = song
            self.play_count[self.song_id] = 0
            self.song_id += 1


    def play_song(self, song_id):
        # how much money to play song??
        if self.money_inserted >= self.price:
            # make change??
            self.total_collected += self.price
            self.money_inserted = 0

            self.play_count[song_id] += 1
            return self.music_menu[song_id]
        else:
            return None


    def insert_money(self, value):
        self.money_inserted += value


