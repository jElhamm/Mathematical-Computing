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

    # # DFT algorithm (2)          ===>           Function np.fft
    # def calculate_DFT(self):
    #     self.X = np.fft.fft(self.x)


# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def  banner():
    print("""
        
#############################################################################################
                                 ***   Welcome   ***                                         
                                                                                                          
               You can use this program to calculate the Fourier transform.                  
                                                                                             
    ____________________________________________________________________________________          
   | The formula used for calculation is:   X_k = Σ(x[n] * e^(-j * 2π * k * n / N)) "   |    
   |____________________________________________________________________________________|   
   | 1 |  X_k  --> The value of the Discrete Fourier Transform at frequency k           |    
   |____________________________________________________________________________________|    
   | 2 |  x[n] --> Input signal at time n                                               |    
   |____________________________________________________________________________________|    
   | 3 |  e    --> Euler's number                                                       |    
   |____________________________________________________________________________________|    
   | 4 |  e^(-j * 2π * k * n / N) --> The inverse exponential function                  |    
   |____________________________________________________________________________________|    
                                                                                                 
#############################################################################################
    """)

def main():
    banner()
    N = int(input("==> Enter the number of samples (N): "))
    calculator = DFTCalculator(N)
    calculator.calculateInputValues()
    calculator.calculate_DFT()
    calculator.print_results()
    print("*********************************************************************\n")
    
if __name__ == "__main__":
    main()

# An example of how to use the program is shown.
