# You can use this program to calculate the Fourier transform.
#  ****    The purpose of this program is to further implement the FFT algorithm.    ****

#   formula is implemented as follows:     X[k] = even.X[k] + exp(-2 π i k / N) * odd.X[k]
#                                          X[k+N/2] = even.X[k] - exp(-2 π i k / N) * odd.X[k]


import numpy as np

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

    # FFT algorithm (2)          ===>           Function np.fft
    # def fft(self):
    #     self.X = np.fft.fft(self.x)


# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def  banner():
    print("""
        
#################################################################################
#                              ***   Welcome   ***                              #
#                                                                               #             
#         You can use this program to calculate the Fourier transform.          #
#        _____________________________________________________________          #
#       |                                                             |         #  
#       |        The formula implemented in this function is          |         #
#       |     the recursive FFT formula, which can be written as:     |         #
#       |                                                             |         #
#       |       X[k] = even.X[k] + exp(-2 π i k / N) * odd.X[k]       |         #
#       |     X[k+N/2] = even.X[k] - exp(-2 π i k / N) * odd.X[k]     |         #
#       |_____________________________________________________________|         #
#                                                                               # 
#        Note(1): Where X[k] is the k-th element of the output sequence,        #
#                 even.X[k] and odd.X[k] are the k-th elements of the FFTs      #
#                 calculated for the even and odd indices respectively,         #
#                 and N is the length of the input sequence.                    #
#        Note(2): There is also a section in the code that can perform          #
#                 the calculation from the ready function.                      #
#                                                                               #    
#################################################################################
    """)

def main():
    banner()
    N = int(input("==> Enter the number of samples (N): "))
    calculator = FFTCalculator(N)
    calculator.calculateInputValues()
    calculator.fft()
    calculator.print_results()
    print("*******************************************************************\n")
    
if __name__ == "__main__":
    main()

# An example of how to use the program is shown.  

# Note:
#      To use the ready function in numpy, do the following steps:
#           1. See line (43).
#           2. Uncomment the code.
#           3. Comment the FFT algorithm (1) in line (25).