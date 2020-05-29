# Imports of general use
import numpy as np
from convert_mp3_to_wav import convert
from music_loading import music_loading
import pywt
import pywt.data
from ODF_SuperFlux import ODF_SuperFlux
from PeDF import PeDF
import matplotlib.pyplot as plt
from plot_PeDF import plot_PeDF
from plot_ODF import plot_ODF

def helper_data(signal_we_want_to_analyze, nivel_wavelet):

    # Wavelet Decomposition
    N = nivel_wavelet
    coif3 = pywt.Wavelet('coif3')
    coeffs = pywt.wavedec(signal_we_want_to_analyze, coif3, level = N) #cAN, cDN, cD(N-1), cD(N-2), .... based in level = N

    # ODF Generation

    # Empty list of ODFs
    ODF_SET = []
    for index in range(0,len(coeffs)):
        coeff_to_odf = coeffs[index]
        sample_rate = 44100
        frame_size = 4096 #92.8ms

        if index == 0:
            samplerate_equivalente = sample_rate/2**(len(coeffs)-1)
            frame_size_equivalente = frame_size/2**(len(coeffs)-1)
        else:
            samplerate_equivalente = sample_rate/2**(len(coeffs)-index)
            frame_size_equivalente = frame_size/2**(len(coeffs)-index)

        ODF = ODF_SuperFlux(coeff_to_odf, samplerate_equivalente, frame_size_equivalente, frame_size_equivalente/2)
        ODF_SET.append(ODF)

    # PeDF Generation 
    PeDF_FULL_SET = []
    PeDF_PARTIAL_SET = []
    for index in range(0,len(ODF_SET)):
        PeDF1 = PeDF(ODF_SET[index], form = "full")
        PeDF2 = PeDF(ODF_SET[index], form = "partial")
        PeDF_FULL_SET.append(PeDF1)
        PeDF_PARTIAL_SET.append(PeDF2)
    
    return ODF_SET, PeDF_FULL_SET, PeDF_PARTIAL_SET