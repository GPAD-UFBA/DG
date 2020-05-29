import numpy as np
import matplotlib.pyplot as plt

def plot_ODF(ODF):
    plt.figure()
    plt.plot(ODF)
    plt.title('ODF')
    plt.ylabel('Onset Strength')
    plt.xlabel('Amostras')