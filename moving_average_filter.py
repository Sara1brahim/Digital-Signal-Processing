import matplotlib.pyplot as plt

def moving_average_filter(signal):
    window = 3

    filtered = []

    for i in range(len(signal)):
        sum_val = 0
        count = 0

        for j in range(window):
            if i - j >= 0:
                sum_val += signal[i - j]
                count += 1

        filtered.append(sum_val / count)

    plt.plot(signal, label="Original")
    plt.plot(filtered, label="Filtered")
    plt.legend()
    plt.show()