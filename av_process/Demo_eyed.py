import eyed3

audiofile = eyed3.load("smzy.mp3")
audiofile.tag.artist = u"Nobunny"
audiofile.tag.album = u"Love Visions"
audiofile.tag.album_artist = u"Various Artists"
audiofile.tag.title = u"I Am a Girlfriend"
audiofile.tag.track_num = 4
audiofile.tag.save()
