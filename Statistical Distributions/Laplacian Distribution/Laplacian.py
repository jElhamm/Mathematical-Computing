# You can use this program to calculate the (Laplacian Distribution) and (display its Graph).

# Laplacian Distribution formula in mathematics is written as follows:        f(x) = 0.5 * e^(-|x - μ| / b) / b
#                                                                      --->    μ = location parameter
#                                                                      --->    b = scale parameter
#   * The scale parameter is calculated as the square root of 0.5 times the median absolute deviation of the data from the median. *



import numpy as np
import matplotlib.pyplot as plt

class LaplacianDistribution:
    def __init__(self, data):
        self.data = data

    def plot(self):
        b = np.sqrt(0.5) * np.median(np.abs(self.data - np.median(self.data)))  # Calculate the scale parameter of the Laplacian distribution based on the median of the dataset.
        x = np.linspace(min(self.data), max(self.data), 100)                    # Generate 100 evenly spaced values between the minimum and maximum value in the dataset.
        y = 0.5 * np.exp(-np.abs(x - np.median(self.data)) / b) / b              # Calculate the probability density function of the Laplacian distribution for each value in x.

        plt.plot(x, y)
        plt.xlabel('Values')
        plt.ylabel('Probability Density Function')
        plt.title('Laplacian Distribution')
        plt.grid(True)
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
          
****************************************************************************************************
*                  (:               ***   Welcome   ***                 :)                         *
*                                                                                                  *
*    You can use this program to calculate the (Laplacian Distribution) and display its Graph.     *
*                                                                                                  *
****************************************************************************************************
*                                                                                                  *
*           Laplacian Distribution formula in mathematics is written as follows:                   *
*                                                                                                  *
*                             f(x) = 0.5 * e^(-|x - μ| / b) / b                                    *
*                                                                                                  *
*                  ---> μ    = location parameter                                                  *
*                  ---> b    = scale parameter                                                     *
*                                                                                                  *
*          The scale parameter is calculated as the square root of 0.5 times the                   *
*                 median absolute deviation of the data from the median.                           *
*                                                                                                  *
****************************************************************************************************
    """)

def main():
    banner()
    analyzer = DataAnalyzer()
    analyzer.read_data()
    mean = analyzer.calculate_statistics()
    plotter = LaplacianDistribution(analyzer.data)
    plotter.plot()
    print("*********************************************************************\n")


if __name__ == '__main__':
    main()


# An example of how to use the program is shown.