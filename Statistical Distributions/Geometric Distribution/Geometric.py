# You can use this program to calculate the (Geometric Distribution) and (display its Graph).

# Geometric Distribution formula in mathematics is written as follows:
#                   𝑦 = (1-𝑝)^(𝑥-1) * 𝑝    --->   𝑦  = is the probability mass function
#                                          --->   𝑥  = is the input value
#                                          --->   𝑝  = is the probability parameter


import numpy as np
import matplotlib.pyplot as plt

class GeometricDistribution:
    def __init__(self, data):
        self.data = data
        self.prob = 1 / (np.mean(data) + 1)                                  # Calculate the probability parameter (p)

    def plot(self):
        x = np.arange(1, int(max(self.data)) + 1, dtype=int)                 # Generate x-values for the plot as integers
        y = (1 - self.prob)**(x - 1) * self.prob                             # Calculate the Geometric distribution

        plt.stem(x, y, linefmt='C0-', markerfmt='C0o', basefmt='k-')
        plt.xlabel('Values')
        plt.ylabel('Probability Mass Function')
        plt.title('Geometric Distribution (p={})'.format(self.prob))
        plt.grid(True)
        plt.show()
 
class DataAnalyzer:
    def __init__(self):
        self.data = []

    def read_data(self):
        data_input = input("---> Enter a list of numbers (comma-separated): ")
        self.data = [int(x) for x in data_input.split(',')]

    def calculate_statistics(self):
        mean = np.mean(self.data)
        print("Average:", mean)
        return mean
 

# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def banner():
    print("""
        
************************************************************************************
*          (:                 ***   Welcome   ***                     :)           *
*                                                                                  *
*                  You can use this program to calculate the                       *
*                (Geometric Distribution) and (display its Graph).                 *
*                      Just enter your list of numbers.                            *
*                                                                                  *
************************************************************************************
*             The formula for Geometric Distribution is as follows:                * 
*                           𝑦 = (1-𝑝)^(𝑥-1) * 𝑝                                    *
*                                                                                  *
*             ***  𝑦    = probability mass function                                *
*             ***  𝑥    = input value                                              *
*             ***  𝑝    = probability parameter                                    *
*                                                                                  *
************************************************************************************
    """)  

def main():
    banner()
    analyzer = DataAnalyzer()
    analyzer.read_data()
    mean = analyzer.calculate_statistics()
    plotter = GeometricDistribution(analyzer.data)
    plotter.plot()
    print("*********************************************************************\n")


if __name__ == '__main__':
    main()

# An example of how to use the program is shown.