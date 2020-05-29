import numpy as np
import matplotlib.pyplot as plt

def plot_PeDF(PeDF, form):
    
    if form == "full":
        plt.figure()
        x1 = np.arange(-len(PeDF)/2, len(PeDF)/2,1)
        plt.plot(x1,PeDF)
        plt.title('PeDF - Total')
        plt.xlabel('Lags')
        
    if form == "partial":
        plt.figure()
        plt.plot(PeDF)
        plt.title('PeDF - Partial')
        plt.xlabel('Lags')