import numpy as np
from scipy import signal

def PeDF(ODF, form):
    corr = signal.correlate(ODF, ODF, mode='same', method='direct')
    corr = corr / np.max(corr)
    
    if form == "full":
        return corr
    if form == "partial":
        index = np.where(corr == 1)
        index = index[0][0]
        return corr[index:]