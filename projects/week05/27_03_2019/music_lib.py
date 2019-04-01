class Song:
    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __str__(self):
        return self.artist + ' - ' + self.title + ' from ' + self.album + ' - ' + self.length

s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")

print(s.__str__())