import numpy as np
from exponentialSignals import exponential_signals
from sampling_quantization import sampling_quantization
from Fourier import fft_analysis
from Elementary_Discrete_Time_Signals import discrete_signals
from cross_correlation import correlation
from Convolution import convolution
from Z import z_transform
from moving_average_filter import moving_average_filter

def main():
    fs = 1000
    T = 1.0
    t = np.linspace(0, T, int(fs*T), endpoint=False)

    signal = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*150*t)

    exponential_signals()
    discrete_signals()

    sampling_quantization(signal, t)
    fft_analysis(signal, t)
    correlation(signal)
    convolution(signal)
    z_transform(signal)
    moving_average_filter(signal)

if __name__ == "__main__":
    main()