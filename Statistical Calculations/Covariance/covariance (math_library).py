# You can use the program to calculate the covariance.
# Covariance formula in mathematics is written as follows: Cov(x, y) = ∑((xᵢ - μₓ)(yᵢ - μᵧ)) / N
#                                                          ---> xᵢ = Each individual value in the first data set
#                                                          ---> yᵢ = Each individual value in the second data set
#                                                          ---> μₓ = The mean of the first data set
#                                                          ---> μᵧ = The mean of the second data set
#                                                          ---> N  = number of data points


import math

class Covariance:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    # Calculations
    def calculate_covariance(self):
        mean1 = sum(self.data1) / len(self.data1)
        mean2 = sum(self.data2) / len(self.data2)
        covariance = sum((x - mean1) * (y - mean2) for x, y in zip(self.data1, self.data2)) / len(self.data1)
        return covariance

    def print_covariance(self):
        covariance = self.calculate_covariance()
        print("   ---> Covariance:", covariance)
 