# You can use this program to calculate the Fourier transform.
#  ****    The purpose of this program is to further implement the DFT algorithm.    ****

#   formula is implemented as follows:   X_k = Σ(x[n] * e^(-j * 2π * k * n / N))


import numpy as np
class DFTCalculator:
    def __init__(self, N):
        self.N = N
        self.x = []
        self.X = []

    def calculateInputValues(self):
        for n in range(self.N):
            x_n = int(input("==> Enter value for x[{}]: ".format(n)))
            self.x.append(x_n)

    def print_results(self):
        for k, X_k in enumerate(self.X):
            print("X[{}] = {}".format(k, X_k))
            
    # DFT algorithm (1)
    def calculate_DFT(self):
        x = np.array(self.x)                            # Convert input signals to numpy arrays for faster computation
        for k in range(self.N):
            n = np.arange(self.N)
            X_k = np.sum(x * np.exp(-1j * 2 * np.pi * k * n / self.N))
            self.X.append(X_k)

            