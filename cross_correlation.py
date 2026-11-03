import matplotlib.pyplot as plt

def correlation(signal):
    x = signal[:50]
    y = signal[:50]

    nx = len(x)
    ny = len(y)

    lags = list(range(-(ny - 1), nx))
    r = []

    for k in range(-(ny - 1), nx):
        sum_val = 0
        for i in range(nx):
            j = i - k
            if 0 <= j < ny:
                sum_val += x[i] * y[j]
        r.append(sum_val)

    plt.stem(lags, r)
    plt.show()