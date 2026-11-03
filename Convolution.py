import matplotlib.pyplot as plt

def convolution(signal):
    x = signal[:50]
    h = [1, 1]

    nx = len(x)
    nh = len(h)

    y = []

    for n in range(nx + nh - 1):
        sum_val = 0
        for k in range(nh):
            if 0 <= n - k < nx:
                sum_val += x[n - k] * h[k]
        y.append(sum_val)

    plt.stem(range(len(y)), y)
    plt.show()