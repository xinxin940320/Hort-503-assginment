class Song(object):

    def __int__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I will stop right there"])

bulls_on_parade = Song(["They rally around the family",
                         "With pockets full of shells"])
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


class Song(object):

    def __int__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_one_song(self):
        for line in self.lyrics:
            print(line)
remember_me = Song(["Remember me",
    "Though I have to travel far"])
rememer_me_more = Song(["That song is not over"])

remember_me.sing_me_one_song()
rememer_me_more.sing_me_one_song()
