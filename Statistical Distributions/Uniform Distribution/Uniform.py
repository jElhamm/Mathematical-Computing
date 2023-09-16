# You can use this program to calculate the (Uniform Distribution) and (display its Graph).

# Uniform Distribution formula in mathematics is written as follows:        𝑦 = 1 / (𝑏 - 𝑎)
#                                                                     --->  𝑦 = probability density function
#                                                                     --->  𝑎 = minimum value
#                                                                     --->  𝑏 = maximum value



import numpy as np
import matplotlib.pyplot as plt

class UniformDistribution:
    def __init__(self, data):
        self.data = data

    def plot(self):
        min_value = min(self.data)
        max_value = max(self.data)
        probability = 1 / (max_value - min_value)

        x = np.linspace(min_value, max_value, 100)
        y = np.full_like(x, probability)

        plt.plot(x, y)
        plt.xlabel('Values')
        plt.ylabel('Probability Density Function')
        plt.title('Uniform Distribution')
        plt.grid(True)
        plt.show()
 