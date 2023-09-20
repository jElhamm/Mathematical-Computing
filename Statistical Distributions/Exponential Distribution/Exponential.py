# You can use this program to calculate the (Uniform Distribution) and (display its Graph).

# Uniform Distribution formula in mathematics is written as follows:        f(x) = λ * e^(-λ * x)
#                                                                      --->    λ = rate parameter 
#                                                                      --->    x = random variable
#                                                                      ---> The rate parameter is calculated as the inverse of the mean of the data.



import numpy as np
import matplotlib.pyplot as plt

class ExponentialDistribution:
    def __init__(self, data):
        self.data = data

    def plot(self):
        rate_parameter = 1 / np.mean(self.data)                    # Calculate the rate parameter of the exponential distribution based on the mean of the dataset.
        x = np.linspace(0, max(self.data), 100)                    # Generate 100 evenly spaced values between 0 and the maximum value in the dataset.
        y = rate_parameter * np.exp(-rate_parameter * x)           # Calculate the probability density function of the exponential distribution for each value in x.

        plt.plot(x, y)
        plt.xlabel('Values')
        plt.ylabel('Probability Density Function')
        plt.title('Exponential Distribution')
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
 