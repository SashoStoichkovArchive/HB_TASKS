class Song:
    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __str__(self):
        return self.artist + ' - ' + self.title + ' from ' + self.album + ' - ' + self.length

    def length_of(self, seconds=False, minutes=False, hours=False):
        counter = 0
        for el in self.length:
            if el == ':':
                counter += 1

        if counter == 2:
            if len(self.length) == 8:
                h = int(self.length[:2])
                m = int(self.length[3:5])
                s = int(self.length[6:])

            if len(self.length) == 7:
                h = int(self.length[:1])
                m = int(self.length[2:4])
                s = int(self.length[5:])

        elif counter == 1:
            if len(self.length) == 5:
                m = int(self.length[:2])
                s = int(self.length[3:])

            if len(self.length) == 4:
                m = int(self.length[:1])
                s = int(self.length[2:])

        if seconds == True:
            if counter == 2:
                return s + (m*60) + (h*3600)
            elif counter == 1:
                return s + (m*60)

        elif minutes == True:
            if counter == 2:
                return m + (h*60)
            elif counter == 1:
                return m

        elif hours == True:
            if counter == 2:
                return h
            elif counter == 1:
                return 0

        else:
            return str(self.length)

class Playlist(Song):
    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.songs = []

    def add_song(self, song):
        if isinstance(song, Song):
            self.songs.append(song)

    def remove_song(self, song):
        if isinstance(song, Song):
            self.songs.remove(song)

    def total_length(self):
        total_sec = 0
        for song in self.songs:
            if isinstance(song, Song):
                total_sec += song.length_of(seconds=True)

        total_sec, s = divmod(total_sec, 60)
        h, m = divmod(total_sec, 60)

        if h == 0:
            return "%02d:%02d" % (m, s)
        else:
            return "%d:%02d:%02d" % (h, m, s)

s1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
s2 = Song(title="The Sons of Odin", artist="Manowar", album="The Sons of Odin", length="6:26")

# print(s1.__str__())
# print(s1.length_of(minutes=True))

p = Playlist(name="Pesho")
# print(p.songs)
p.add_song(s1)
# print(p.songs)
p.add_song(s2)
# print(p.songs)
# p.remove_song(s1)
# print(p.songs)

print(p.total_length())