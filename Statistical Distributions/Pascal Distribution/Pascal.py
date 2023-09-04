# You can use this program to calculate the (Pascal Distribution) and (display its Graph).

# The Pascal Distribution Probability Mass Function (PMF):
#    PMF(x) = C(x + r - 1, x) * p^r * (1 - p)^x     --->   C(n, k) = the binomial coefficient.
#                                                   --->   x = number of failures before the rth success occurs.
#                                                   --->   r = number of successes.
#                                                   --->   p = probability of success.


import numpy as np
from math import factorial
import matplotlib.pyplot as plt


class PascalDistribution:
    def __init__(self, data):
        self.data = data
        self.p = 1 / (int(np.mean(data)) + 1)                   # Calculate the probability parameter (p)
        self.r = int(np.mean(data))                             # Calculate the number of successes parameter (r)

    def pmf(self, x):
        """
            This function calculates the probability mass function (PMF) of a negative binomial distribution.
            Args:
                x (int): The number of successes.
    
            Returns:
                float: The probability of obtaining 'x' successes in a negative binomial distribution.
        """
        return (factorial(x + self.r - 1) // (factorial(x) * factorial(self.r - 1))) * (self.p ** self.r) * ((1 - self.p) ** x)

    def plot(self):
        x = np.arange(0, int(max(self.data)) + 1)               # Generate x-values for the plot as integers
        y = [self.pmf(xi) for xi in x]                          # Calculate the Pascal distribution

        plt.stem(x, y, linefmt='C0-', markerfmt='C0o', basefmt='k-')
        plt.xlabel('Values')
        plt.ylabel('Probability Mass Function')
        plt.title('Pascal Distribution (r={}, p={})'.format(self.r, self.p))
        plt.grid(True)
        plt.show()
 