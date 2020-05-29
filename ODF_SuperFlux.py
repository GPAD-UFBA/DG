# Now we're gonna try making an ODF with SuperFlux!
# REF: https://madmom.readthedocs.io/en/latest/modules/audio/signal.html
# REF: https://madmom.readthedocs.io/en/latest/modules/audio/spectrogram.html
# REF: https://madmom.readthedocs.io/en/latest/modules/features/onsets.html
# REF: Sebastian Böck and Gerhard Widmer, “Maximum Filter Vibrato Suppression for Onset Detection”, Proceedings of the 16th International Conference on Digital Audio Effects (DAFx), 2013.
# Onset: SuperFlux 
import numpy as np
import matplotlib.pyplot as plt
import madmom

def ODF_SuperFlux(signal, sample_rate, frame_size, hop):
    
    # Loading a file with desired sample_rate and down-mixed
    sig = madmom.audio.signal.Signal(signal, sample_rate = sample_rate, num_channels = 1)

    # We frame the signal
    frames = madmom.audio.signal.FramedSignal(sig, frame_size=frame_size, hop=hop)

    # We compute the log filtered spectrogram of each frame, the number of bands is fixed based in the documentation
    log_filt_spec = madmom.audio.spectrogram.LogarithmicFilteredSpectrogram(frames, num_bands = 24)

    # We compute the ODF presented in Bock et tal (2013)
    odf_raw = madmom.features.onsets.superflux(log_filt_spec)
    odf_raw = np.array(odf_raw)
    odf_raw = odf_raw / np.max(odf_raw)
    
    return odf_raw