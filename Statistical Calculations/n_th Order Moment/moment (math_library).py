# You can use the program to calculate the (n_th Order Moment).

# n_th Order Moment formula in mathematics is written as follows:    (1/N) * Σ((xi - mean)^n)
#                                                               --->  N is the number of data points in the dataset
#                                                               --->  xi is the ith data point
#                                                               --->  mean is the mean of the dataset
#                                                               --->  n is the order of the moment


import math

class Moment:
    def __init__(self, data):
        self.data = data

    # Calculations
    def calculate_nth_order_moment(self, n):
        mean = sum(self.data) / len(self.data)                              # Calculate the mean
        moment = sum((x - mean) ** n for x in self.data) / len(self.data)   # Calculate the moment
        return moment

    def print_moment(self, n):
        moment = self.calculate_nth_order_moment(n)
        print("   --->", n, "th order moment:", moment)
 

# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def banner():
    print("""
        
################################################################################
#                           ***   Welcome   ***                                #
#                                                                              #
#        You can use the program to calculate the (n_th Order Moment).         #
#                _____________________________________________                 #
#               |                                             |                #
#               |   he formula for variance is as follows:    |                #
#               |    (1/N) * Σ((xi - mean)^n)                 |                #
#               |_____________________________________________|                #
#                                                                              #
#          --->    N    = is the number of data points in the dataset          #
#          --->    Σ    = sum of                                               #
#          --->    xi   = is the ith data point                                #
#          --->    mean = is the mean of the dataset                           #
#          --->    n    = is the order of the moment                           #
#                                                                              #
################################################################################
    """)

def main():
    banner()
    data = input("   ---> Enter a list of data (separated by spaces): ").split()
    data = [float(x) for x in data]
    n = int(input("   ---> Enter the order of the moment: "))
    moment_calculator = Moment(data)
    print("\n**********************************************************************************")
    moment_calculator.print_moment(n)
    print("**********************************************************************************\n")

if __name__ == "__main__":
    main()

# An example of how to use the program is shown.