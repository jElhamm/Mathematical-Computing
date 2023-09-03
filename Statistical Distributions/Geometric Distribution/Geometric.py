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
 