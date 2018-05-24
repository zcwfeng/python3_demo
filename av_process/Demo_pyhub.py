from pydub import AudioSegment

# song = AudioSegment.from_wav("never_gonna_give_you_up.wav")
# song = AudioSegment.from_mp3("never_gonna_give_you_up.mp3")
#
# ogg_version = AudioSegment.from_ogg("never_gonna_give_you_up.ogg")
# flv_version = AudioSegment.from_flv("never_gonna_give_you_up.flv")
#
# mp4_version = AudioSegment.from_file("never_gonna_give_you_up.mp4", "mp4")
# wma_version = AudioSegment.from_file("never_gonna_give_you_up.wma", "wma")
# aac_version = AudioSegment.from_file("never_gonna_give_you_up.aiff", "aac")
song = AudioSegment.from_mp3("smzy.mp3")
song.export("out.ogg", format="ogg")  # Is the same as:
# song.export("out.ogg", format="ogg", codec="libvorbis")
