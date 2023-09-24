# You can use this program to calculate the (Gamma Distribution) and (display its Graph).

# Gamma Distribution formula in mathematics is written as follows:        
#               f(x) = (x^(k-1) * e^(-x/θ)) / (θ^k * Γ(k))
#          --->  'x' is the random variable
#          --->  'k' is the shape parameter
#          --->  'θ' is the scale parameter, which is equal to the mean divided by k
#          --->  'e' is the base of the natural logarithm
#          --->  'Γ' is the gamma function, which is a generalization of the factorial function to non-integer values.



import math
import numpy as np
import matplotlib.pyplot as plt

class GammaDistribution:
    def __init__(self, data, k):
        self.data = data
        self.k = k

def plot(self):
    # Calculate the scale parameter (theta) using the mean of the data and the shape parameter (k)
    theta = np.mean(self.data) / self.k
    
    # Generate 100 equally spaced values between 0 and the maximum value in the data
    x = np.linspace(0, max(self.data), 100)
    
    # Calculate the probability density function (PDF) for each value in x using the Gamma Distribution formula
    y = (x ** (self.k - 1) * np.exp(-x / theta)) / (theta ** self.k * math.gamma(self.k))
    
    plt.plot(x, y)
    plt.xlabel('Values')
    plt.ylabel('Probability Density Function')
    plt.title('Gamma Distribution')
    plt.grid(True)                                                      # Add a grid to the graph
    plt.show()
  
class DataAnalyzer:
    def __init__(self):
        self.data = []

    def read_data(self):
        data_input = input("---> Enter a list of numbers (comma-separated): ")
        self.data = [float(x.strip()) for x in data_input.split(',')]

    def calculate_statistics(self):
        mean = np.mean(self.data)
        print("---> Mean:", mean)
        return mean
 

# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def banner():
    print("""
          
******************************************************************************************************************************
*                              (:               ***   Welcome   ***                 :)                                       *
*                                                                                                                            *
*                    You can use this program to calculate the (Gamma Distribution) and display its Graph.                   *
*                                                                                                                            *
******************************************************************************************************************************
*       Gamma Distribution formula in mathematics is written as follows:   f(x) = (x^(k-1) * e^(-x/θ)) / (θ^k * Γ(k))        *
*                                                                                                                            *
*          --->  'x' is the random variable                                                                                  *
*          --->  'k' is the shape parameter                                                                                  *
*          --->  'θ' is the scale parameter, which is equal to the mean divided by k                                         *
*          --->  'e' is the base of the natural logarithm                                                                    *
*          --->  'Γ' is the gamma function, which is a generalization of the factorial function to non-integer values.       *
*                                                                                                                            *
******************************************************************************************************************************
    """)

def main():
    banner()
    analyzer = DataAnalyzer()
    analyzer.read_data()
    k = float(input("---> Enter the shape parameter (k): "))
    mean = analyzer.calculate_statistics()
    plotter = GammaDistribution(analyzer.data, k)
    plotter.plot()
    print("*********************************************************************\n")

if __name__ == '__main__':
    main()


# An example of how to use the program is shown.