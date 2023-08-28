# You can use the program to calculate the (Standard Deviation).

# The formula for standard deviation is as follows:         σ = √(Σ(xi - μ)² / N)
#                                                   --->    xi = individual data point
#                                                   --->    μ = mean (average)
#                                                   --->    N = number of data points


import statistics

class StandardDeviation:
    def __init__(self, data):
        self.data = data

    # Calculations
    def calculate_standardDeviation(self):
        return statistics.stdev(self.data)

    def print_standardDeviation(self):
        standardDeviation = self.calculate_standardDeviation()
        print("   ---> Standard Deviation:", standardDeviation)
