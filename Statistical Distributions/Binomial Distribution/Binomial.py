# You can use this program to calculate the (Binomial Distribution) and (display its Graph).
# Binomial Distribution formula in mathematics is written as follows:

#              ***     PMF(k) = C(n, k) * p^k * (1 - p)^(n - k)     ***

#  --->  PMF(k)  = probability of obtaining 'k' successes in a binomial distribution.
#  --->  C(n, k) = binomial coefficient, calculated as n! / (k! * (n - k)!), which represents the number of ways to choose 'k' successes from 'n' trials.
#  --->  p = probability of success for each trial.
#  --->  n = total number of trials.



import math
import numpy as np
import matplotlib.pyplot as plt

class BinomialDistribution:
    def __init__(self, n, p):
        self.n = n                   # Number of trials
        self.p = p                   # Probability of success

    def pmf(self, k):
        """
        This function calculates the probability mass function (PMF) of a binomial distribution.
        Args:
            k (int): The number of successes for which to calculate the probability mass function.
        Returns:
            float: The probability of obtaining 'k' successes in a binomial distribution.
        """
        coef = math.comb(self.n, k)                                         # Calculate the binomial coefficient
        return coef * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def plot(self):
        x = np.arange(0, self.n + 1)                                        # Generate x-values for the plot
        y = [self.pmf(k) for k in x]                                        # Calculate the binomial distribution

        plt.bar(x, y)
        plt.xlabel('Number of Successes')
        plt.ylabel('Probability Mass Function')
        plt.title('Binomial Distribution (n={}, p={})'.format(self.n, self.p))
        plt.grid(True)
        plt.show()
 
class DataAnalyzer:
    def __init__(self):
        self.data = []

    def read_data(self):
        data_input = input("---> Enter the number of trials (n): ")
        self.n = int(data_input)
        
        p_input = input("---> Enter the probability of success (p): ")
        self.p = float(p_input)
        
        # Check if p is within the valid range
        if self.p < 0 or self.p > 1:
            raise ValueError(" ( ! Invalid input. The probability of success (p) must be between 0 and 1. ! )")
        
        # Check if n is a positive integer
        if self.n <= 0 or not isinstance(self.n, int):
            raise ValueError(" ( ! Invalid input. The number of trials (n) must be a positive integer. ! )")

    def calculate_statistics(self):
        mean = self.n * self.p
        print("---> Average:", mean)
        return mean
 