import numpy as np
import madmom

def music_loading(filename, sample_rate=44100):
    sig = madmom.audio.signal.Signal(filename, sample_rate = sample_rate, num_channels = 1)
    musica = np.array(sig)
    musica = musica/np.max(np.abs(musica))
    return musica