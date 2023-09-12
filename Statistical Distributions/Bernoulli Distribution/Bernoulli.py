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
 
class DataAnalyzer:
    def __init__(self):
        self.data = []

    def read_data(self):
        data_input = input("Enter a list of numbers (comma-separated), (All values must be either 0 or 1): ")
        self.data = [int(x) for x in data_input.split(',')]

        # Check if all values are either 0 or 1
        if not all(x in [0, 1] for x in self.data):
            raise ValueError("Invalid input. All values must be either 0 or 1.")

    def calculate_statistics(self):
        mean = np.mean(self.data)
        print("Average:", mean)
        return mean
 

# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def banner():
    print("""
          
**********************************************************************************
*             (:               ***   Welcome   ***                 :)            *
*                                                                                *
*                 You can use this program to calculate the                      *
*              (Bernoulli Distribution) and display its Graph.                   *
*                                                                                *
**********************************************************************************
*                                                                                *
*         The Bernoulli Distribution Probability Mass Function (PMF):            *
*                    PMF(x) = p^x * (1 - p)^(1 - x)                              *
*                                                                                *
*          --->   x   = 0 or 1 (the possible values in the distribution)         *
*          --->   p   = probability of success                                   *
*                                                                                *
**********************************************************************************
    """)


def main():
    banner()
    analyzer = DataAnalyzer()
    analyzer.read_data()
    mean = analyzer.calculate_statistics()
    plotter = BernoulliDistribution(analyzer.data)
    plotter.plot()
    print("****************************************************************\n")

if __name__ == '__main__':
    main()

# An example of how to use the program is shown.