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
 