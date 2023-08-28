# You can use the program to calculate the covariance.
# Covariance formula in mathematics is written as follows: Cov(x, y) = ∑((xᵢ - μₓ)(yᵢ - μᵧ)) / N
#                                                          ---> xᵢ = Each individual value in the first data set
#                                                          ---> yᵢ = Each individual value in the second data set
#                                                          ---> μₓ = The mean of the first data set
#                                                          ---> μᵧ = The mean of the second data set
#                                                          ---> N  = number of data points


import statistics

class Covariance:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    # Calculations
    def calculate_covariance(self):
        return statistics.covariance(self.data1, self.data2)

    def print_covariance(self):
        covariance = self.calculate_covariance()
        print("   ---> Covariance:", covariance)
