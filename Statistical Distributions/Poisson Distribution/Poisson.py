# You can use this program to calculate the (Poisson Distribution) and (display its Graph).

# Poisson Distribution formula in mathematics is written as follows:
#  𝑦 = (𝑒^−𝜆 * 𝜆^𝑥) / 𝑥!      --->  y = probability mass function
#                             --->  𝑥 = input value
#                             --->  𝜆 = mean or average rate of the event
#                             ---> 𝑥! = factorial of 𝑥
#                             --->  𝑒 = mathematical constant Euler's number (approximately 2.71828)


import math
import numpy as np
import matplotlib.pyplot as plt

class PoissonDistribution:
    def __init__(self, data):
        self.data = data
        self.mean = np.mean(data)

    def plot(self):
        x = np.arange(0, int(max(self.data)) + 1, dtype=int)                                   # Generate x-values for the plot as integers
        y = (np.exp(-self.mean) * self.mean**x) / np.array([math.factorial(i) for i in x])     # Calculate the Poisson distribution

        plt.stem(x, y, use_line_collection=True)                                               # Plot the Poisson distribution (stem plot)
        plt.xlabel('Values')
        plt.ylabel('Probability Mass Function')
        plt.title('Poisson Distribution (mean={})'.format(self.mean))                          # Add title to the plot with mean and standard deviation values
        plt.grid(True)                                                                         # Display grid lines
        plt.show()
  