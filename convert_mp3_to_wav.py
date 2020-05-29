from pydub import AudioSegment

def convert(filename):
    # Convert .mp3 to .wav
    # filename = "example.mp3"
    sound = AudioSegment.from_mp3(filename)
    soundwav = sound.export(filename[:-4] + ".wav", format="wav")
    soundwav.close()