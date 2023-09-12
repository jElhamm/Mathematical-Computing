# You can use this program to calculate the (Bernoulli Distribution) and (display its Graph).

# Bernoulli Distribution formula in mathematics is written as follows:
#  PMF(x) = p^x * (1 - p)^(1 - x)       --->  x =  possible values in the distribution (x = 0 or 1)
#                                       --->  p =  probability of success



import numpy as np
import matplotlib.pyplot as plt


class BernoulliDistribution:
    def __init__(self, data):
        self.data = data
        self.p = np.mean(data)                      # Calculate the probability parameter (p)

    def pmf(self, x):
        """
        This function calculates the probability mass function (PMF) of a Bernoulli distribution.
        Args:
            x (int): The value for which to calculate the probability mass function.
        Returns:
            float: The probability of obtaining 'x' in a Bernoulli distribution.
        """
        return self.p if x == 1 else 1 - self.p

    def plot(self):
        x = [0, 1]                                  # Generate x-values for the plot
        y = [self.pmf(xi) for xi in x]              # Calculate the Bernoulli distribution

        plt.bar(x, y)
        plt.xlabel('Values')
        plt.ylabel('Probability Mass Function')
        plt.title('Bernoulli Distribution (p={})'.format(self.p))
        plt.xticks(x)
        plt.yticks(np.arange(0, 1.1, 0.1))
        plt.grid(True)
        plt.show()
 