class Song: 
    def __init__(self, artist, track_ttile, album, year):
        self.artist = artist
        self.track_title = track_ttile
        self.album = album
        self.year = year

    def __str__(self):
        return f'{self.artist}\n{self.track_title}\n{self.album}\n{self.year}'
    
song1 = Song('nirvana', 'Lounge Act', 'Nevermind', '1992')
song2 = Song('jack off jill', 'strawberry gashes', 'clear hearts gray flowers', '2000')
print(f'{song1}\n{song2}')