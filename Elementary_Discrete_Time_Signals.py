import numpy as np
import matplotlib.pyplot as plt

def discrete_signals():
    k = 2
    a = 100
    n = np.arange(-5,6,1,dtype=float)

    Unit_Sample = np.where(n+k==0,1,0)*a
    Unit_Step = np.where(n>=0,1,0)
    Unit_Ramp = np.where(n>=0,n,0)

    plt.figure(figsize=(10,10))

    plt.subplot(2,2,1)
    plt.stem(n,Unit_Sample)

    plt.subplot(2,2,2)
    plt.stem(n,Unit_Step)

    plt.subplot(2,2,3)
    plt.stem(n,Unit_Ramp)

    plt.show()