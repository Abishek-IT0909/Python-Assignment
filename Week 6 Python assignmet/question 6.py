import random


class Playlist:
    def __init__(self):
        self.songs = []

    def shuffle(self):
        random.shuffle(self.songs)


my_playlist = Playlist()
my_playlist.songs.append({"title": "Cocaine","artist":"Eric Clapton"})
my_playlist.songs.append({"title": "TNT","artist": "ACDC"})
my_playlist.songs.append({"title": "Nokia","artist": "drake"})
my_playlist.songs.append({"title": "A lot", "artist": "21 savage"})
my_playlist.songs.append({"title": "Mr Toot","artist": "Ylvis"})

my_playlist.shuffle()

for song in my_playlist.songs:
    print(f"Title: {song['title']}, Artist: {song['artist']}")