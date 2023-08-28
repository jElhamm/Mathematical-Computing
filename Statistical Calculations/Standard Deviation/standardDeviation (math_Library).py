# You can use the program to calculate the (Standard Deviation).

# The formula for standard deviation is as follows:         σ = √(Σ(xi - μ)² / N)
#                                                   --->    xi = individual data point
#                                                   --->    μ = mean (average)
#                                                   --->    N = number of data points


import math

class StandardDeviation:
    def __init__(self, data):
        self.data = data
        self.mean = self.calculate_mean()

    def calculate_mean(self):
        total = sum(self.data)
        n = len(self.data)
        return total / n
    
    # Calculations
    def calculate_standardDeviation(self):
        squared_diff = [(x - self.mean) ** 2 for x in self.data]
        sum_squared_diff = sum(squared_diff)
        n = len(self.data)
        standard_deviation = math.sqrt(sum_squared_diff / n)
        return standard_deviation

    def print_standardDeviation(self):
        standard_deviation = self.calculate_standardDeviation()
        print("   ---> Standard Deviation:", standard_deviation)


# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def  banner():
    print("""
        
################################################################################
#                              ***   Welcome   ***                             #
#                                                                              #             
#        You can use the program to calculate the (Standard Deviation).        #
#          
#              The formula for standard deviation is as follows:               #
#                           σ = √(Σ(xi - μ)² / N)                              #
#                   --->    σ = standard deviation                             #
#                   --->    Σ = sum of                                         #
#                   --->    xi = individual data point                         #
#                   --->    μ = mean (average)                                 #
#                   --->    N = number of data points                          #
#                                                                              #    
################################################################################
    """)

def main():
    banner()
    data = input("   ---> Enter a list of data (separated by spaces): ").split()
    data = [float(x) for x in data]
    standard_deviation_calculator = StandardDeviation(data)
    print("\n**********************************************************************************")
    standard_deviation_calculator.print_standardDeviation()
    print("**********************************************************************************\n")


if __name__ == "__main__":
    main()

# An example of how to use the program is shown.