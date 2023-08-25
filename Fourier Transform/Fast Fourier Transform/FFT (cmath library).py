# You can use this program to calculate the Fourier transform.
#  ****    The purpose of this program is to further implement the FFT algorithm.    ****

#   formula is implemented as follows:     X[k] = even.X[k] + exp(-2 π i k / N) * odd.X[k]
#                                          X[k+N/2] = even.X[k] - exp(-2 π i k / N) * odd.X[k

import cmath

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

   # FFT algorithm
    def calculate_FFT(self):
        if self.N <= 1:                                              # Base case for recursion
            self.X = self.x
        else:
            even = FFTCalculator(self.N // 2)                        # Create object for even indices
            odd = FFTCalculator(self.N // 2)                         # Create object for odd indices
            even.x = [self.x[i] for i in range(0, self.N, 2)]        # Extract even indices from input sequence
            odd.x = [self.x[i] for i in range(1, self.N, 2)]         # Extract odd indices from input sequence

            even.calculate_FFT()                                     # Recursively calculate FFT for even indices
            odd.calculate_FFT()                                      # Recursively calculate FFT for odd indices
            self.X = [0] * self.N                                    # Initialize output sequence

            for k in range(self.N // 2):                             # Compute elements of the output sequence
                t = cmath.exp(-2j * cmath.pi * k / self.N) * odd.X[k]
                self.X[k] = even.X[k] + t
                self.X[k + self.N // 2] = even.X[k] - t

# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def  banner():
    print("""
        
################################################################################
#                              ***   Welcome   ***                             #
#                                                                              #             
#         You can use this program to calculate the Fourier transform.         #
#        _____________________________________________________________         #
#       |                                                             |        #  
#       |        The formula implemented in this function is          |        #
#       |     the recursive FFT formula, which can be written as:     |        #
#       |                                                             |        #
#       |       X[k] = even.X[k] + exp(-2 π i k / N) * odd.X[k]       |        #
#       |     X[k+N/2] = even.X[k] - exp(-2 π i k / N) * odd.X[k]     |        #
#       |_____________________________________________________________|        #
#                                                                              # 
#        Note:   Where X[k] is the k-th element of the output sequence,        #
#                even.X[k] and odd.X[k] are the k-th elements of the FFTs      #
#                calculated for the even and odd indices respectively,         #
#                and N is the length of the input sequence.                    #
#                                                                              #    
################################################################################
    """)

def main():
    banner()
    N = int(input("==> Enter the number of samples (N): "))
    calculator = FFTCalculator(N)
    calculator.calculateInputValues()
    calculator.calculate_FFT()
    calculator.print_results()
    print("*******************************************************************\n")
    
if __name__ == "__main__":
    main()

# An example of how to use the program is shown.