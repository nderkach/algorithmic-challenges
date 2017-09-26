import random

denominations = [1, 5, 10, 25, 50]

class Coin(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value) 

class Song(object):
    def __init__(self, band, title, price):
        self.title = title
        self.band = band
        self.price = price

    def __str__(self):
        return "{} by {}".format(self.title, self.band)

class Jukebox(object):
    def __init__(self):
        self.current_balance = 0
        self.songs = [Song("Darude", "Sandstorm", random.randint(25, 50)) for _ in range(1, random.randint(1, 10))]

    def insert_coin(self, coin):
        self.current_balance += coin.value

    def play_song_with_number(self, song_number):
        if song_number >= len(self.songs):
            print("Incorrect song id: {}".format(song_number))
            return False

        song = self.songs[song_number]
        print("Current balance:", self.current_balance)
        print("Song price:", song.price)

        if self.current_balance < song.price:
            print('Insufficient balance: {} | Song Price: {}'.format(self.current_balance, song.price))
            return False
        else:
            self.current_balance -= song.price
            print('Playing song:', str(song))


coins = [Coin(random.choice(denominations)) for _ in range(10)]
for c in coins:
    print(c)

j = Jukebox()
j.insert_coin(coins.pop()) 
j.insert_coin(coins.pop()) 
j.play_song_with_number(1)
j.play_song_with_number(1)

