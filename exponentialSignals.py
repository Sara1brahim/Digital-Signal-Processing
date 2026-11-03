import numpy as np
import matplotlib.pyplot as plt

def exponential_signals():
    n = np.arange(-5, 6, 1, dtype=float)

    a1 = .8
    a2 = 2
    a3 = -.8
    a4 = -2

    S1 = a1 ** n
    S2 = a2 ** n
    S3 = a3 ** n
    S4 = a4 ** n

    plt.figure(figsize=(10,10))

    plt.subplot(2,2,1)
    plt.stem(n,S1)
    plt.title("Signal 1")

    plt.subplot(2,2,2)
    plt.stem(n,S2)
    plt.title("Signal 2")

    plt.subplot(2,2,3)
    plt.stem(n,S3)
    plt.title("Signal 3")

    plt.subplot(2,2,4)
    plt.stem(n,S4)
    plt.title("Signal 4")

    plt.tight_layout()
    plt.show()