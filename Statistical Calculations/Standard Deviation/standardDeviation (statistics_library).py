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
    data = input("   ---> Enter a list of data (separated by spaces): ").split()
    data = [float(x) for x in data]
    standardDeviation_calculator = StandardDeviation(data)
    print("\n**********************************************************************************")
    standardDeviation_calculator.print_standardDeviation()
    print("**********************************************************************************\n")

if __name__ == "__main__":
    main()

# An example of how to use the program is shown.  