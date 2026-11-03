import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

def fft_analysis(signal, t):
    fs = int(1 / (t[1] - t[0]))

    N = len(signal)
    yf = fft(signal)
    xf = fftfreq(N, 1/fs)

    xf = xf[:N//2]
    yf = 2.0/N * np.abs(yf[:N//2])

    plt.figure(figsize=(10,4))

    plt.subplot(1,2,1)
    plt.plot(t, signal)

    plt.subplot(1,2,2)
    plt.plot(xf, yf)

    plt.show()