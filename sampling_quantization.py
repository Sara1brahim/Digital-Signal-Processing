import numpy as np
import matplotlib.pyplot as plt

def sampling_quantization(signal, t):
    fs = 100
    ts = np.arange(0, 1, 1/fs)

    step = int(len(signal) / len(ts))
    sampled_signal = signal[::step]

    quantizing_bits = 4
    quantizing_levels = 2 ** quantizing_bits

    max_val = 1
    min_val = -1

    delta = (max_val - min_val) / quantizing_levels

    quantizing_signal = np.round((sampled_signal - min_val) / delta) * delta + min_val

    plt.figure(figsize=(10,10))

    plt.subplot(1,2,1)
    plt.plot(t, signal)
    plt.stem(ts, sampled_signal, linefmt="r")

    plt.subplot(1,2,2)
    plt.stem(ts, quantizing_signal, linefmt="g")

    plt.show()