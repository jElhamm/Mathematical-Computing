# You can use the program to calculate the (Variance).

# Variance formula in mathematics is written as follows:    Var = ∑(xᵢ - μ)² / N
#                                                     --->  xᵢ represents each individual value in the dataset.
#                                                     --->  μ represents the mean of the dataset.
#                                                     --->  N represents the total number of values in the dataset.


import math

class Variance:
    def __init__(self, data):
        self.data = data

    def calculate_mean(self):
        total = sum(self.data)
        mean = total / len(self.data)
        return mean

    # Calculations
    def calculate_variance(self):
        mean = sum(self.data) / len(self.data)                         # Calculate the mean
        sum_of_squares = sum((x - mean) ** 2 for x in self.data)       # Calculate the sum of squares
        variance = sum_of_squares / len(self.data)                     # Calculate the variance
        return variance

    def print_variance(self):
        variance = self.calculate_variance()
        print("   ---> Variance:", variance)
        