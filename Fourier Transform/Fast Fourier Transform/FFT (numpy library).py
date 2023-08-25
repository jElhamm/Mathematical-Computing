# You can use this program to calculate the Fourier transform.
#  ****    The purpose of this program is to further implement the FFT algorithm.    ****

#   formula is implemented as follows:     X[k] = even.X[k] + exp(-2 π i k / N) * odd.X[k]
#                                          X[k+N/2] = even.X[k] - exp(-2 π i k / N) * odd.X[k]


class FFTCalculator:
    def __init__(self, N):
        self.N = N
        self.x = np.zeros(N, dtype=complex)
        self.X = np.zeros(N, dtype=complex)

    def calculateInputValues(self):
        for n in range(self.N):
            x_n = int(input("==> Enter value for x[{}]: ".format(n)))
            self.x[n] = x_n

    def print_results(self):
        for k, X_k in enumerate(self.X):
            print("X[{}] = {}".format(k, X_k))

    # FFT algorithm (1)
    def fft(self):
        if self.N <= 1:
            self.X = self.x
        else:
            even = FFTCalculator(self.N // 2)
            odd = FFTCalculator(self.N // 2)
            even.x = [self.x[i] for i in range(0, self.N, 2)]        # Extract even indices from input sequence
            odd.x = [self.x[i] for i in range(1, self.N, 2)]         # Extract odd indices from input sequence
            even.fft()
            odd.fft()
            
            # Perform FFT calculation
            for k in range(self.N // 2):
                t = np.exp(-2j * np.pi * k / self.N) * odd.X[k]
                self.X[k] = even.X[k] + t
                self.X[k + self.N // 2] = even.X[k] - t
