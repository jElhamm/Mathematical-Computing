# You can use this program to calculate the Fourier transform.
#  ****    The purpose of this program is to further implement the FFT algorithm.    ****


class FFTCalculator:
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


