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
 

# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def  banner():
    print("""
        
###################################################################################
#                            ***   Welcome   ***                                  #
#                                                                                 #             
#             You can use the program to calculate the (covariance).              #
#                 The formula for covariance is as follows:                       #
#                ___________________________________________                      #
#               |                                           |                     #
#               |   Cov(x, y) = ∑((xᵢ - μₓ)(yᵢ - μᵧ)) / N   |                     #
#               |___________________________________________|                     #
#                                                                                 #
#       --->   Cov(x, y) = represents covariance between the datasets             #
#       --->   Σ = sum of                                                         #
#       --->   xi = represents each individual value in the first dataset         #
#       --->   yi = represents each individual value in the second dataset        #
#       --->   μₓ = represents the mean of the first dataset                      #
#       --->   μᵧ = represents the mean of the second dataset                     #
#       --->   N = represents the total number of values in the datasets          #
#                                                                                 #    
###################################################################################
    """)  

def main():
    banner()
    data1 = input("   ---> Enter a list of data for the first dataset (separated by spaces): ").split()
    data1 = [float(x) for x in data1]
    data2 = input("   ---> Enter a list of data for the second dataset (separated by spaces): ").split()
    data2 = [float(x) for x in data2]
    covariance_calculator = Covariance(data1, data2)
    print("\n**********************************************************************************")
    covariance_calculator.print_covariance()
    print("**********************************************************************************\n")

if __name__ == "__main__":
    main()

# An example of how to use the program is shown.