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
        

# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def  banner():
    print("""
        
################################################################################
#                           ***   Welcome   ***                                #
#                                                                              #
#        You can use the program to calculate the (variance).                  #
#                                                                              #
#        The formula for variance is as follows:                               #
#                Var = ∑(xᵢ - μ)² / N                                          #
#        --->    Var = represents variance                                     #
#        --->    Σ = sum of                                                    #
#        --->    xi = represents each individual value in the dataset          #
#        --->    μ = represents the mean of the dataset                        #
#        --->    N = represents the total number of values in the dataset      #
#                                                                              #
################################################################################
    """)  

def main():
    banner()
    data = input("   ---> Enter a list of data (separated by spaces): ").split()
    data = [float(x) for x in data]
    variance_calculator = Variance(data)
    print("\n**********************************************************************************")
    variance_calculator.print_variance()
    print("**********************************************************************************\n")

if __name__ == "__main__":
    main()

# An example of how to use the program is shown.