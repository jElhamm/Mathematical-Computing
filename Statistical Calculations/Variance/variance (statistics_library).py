# You can use the program to calculate the (Variance).

# Standard deviation formula in mathematics is written as follows:    σ = √((Σ(xi - μ)²) / N)
#                                                               --->  xi represents each individual data point in the dataset.
#                                                               --->  μ represents the mean (average) of the dataset.
#                                                               --->  N represents the total number of data points in the dataset


import statistics

class Variance:
    def __init__(self, data):
        self.data = data

    # Calculations
    def calculate_variance(self):
        return statistics.variance(self.data)

    def print_variance(self):
        variance = self.calculate_variance()
        print("   ---> Variance:", variance)
        