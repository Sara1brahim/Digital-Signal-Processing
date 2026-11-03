import sympy as sp

def z_transform(signal):
    z = sp.symbols('z')

    x = signal[:6]
    index = list(range(len(x)))

    Xz = 0

    for i in range(len(x)):
        Xz += x[i] * z**(-index[i])

    print("X(z) =", Xz)