# You can use this program to calculate the Fourier transform.
#  ****    The purpose of this program is to further implement the DFT algorithm.    ****


import math

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

    # DFT algorithm
    def calculate_DFT(self):
        for k in range(self.N):
            X_k = 0
            for n in range(self.N):
                # Calculate the DFT for each value of k and n
                X_k += self.x[n] * math.e**(-1j * 2 * math.pi * k * n / self.N)
            self.X.append(X_k)


