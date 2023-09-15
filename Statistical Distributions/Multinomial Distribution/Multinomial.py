# You can use this program to calculate the (Multinomial Distribution) and (display its Graph).
# Two types of formulas are implemented in the code.

# (1: Line 28)           result = np.polyval(self.coefficients, x)
# Here, np.polyval is a function from the NumPy library that calculates the value of a polynomial 
# with the given coefficients (self.coefficients) at a specified value of x. This formula allows 
# the code to evaluate the multinomial distribution at a given value of x.

# (2: Line 31)           Use mathematical formula to calculate Multinomial Distribution       



import numpy as np
import matplotlib.pyplot as plt

class MultinomialDistribution:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def evaluate(self, x):
        # Type 1:

        # This function evaluates the multinomial distribution at a given value of x.
        # Args:
        #     x (float): The value at which to evaluate the multinomial distribution.
        # Returns:
        #     float: The result of evaluating the multinomial distribution at x.
        result = np.polyval(self.coefficients, x)
        return result
       
        # Type 2:

        # result = 0
        # for i, coef in enumerate(self.coefficients[::-1]):
        #     result += coef * x**i
        # return result


    def plot(self, x_range):
        x = np.arange(x_range[0], x_range[1], 0.1)
        y = np.polyval(self.coefficients, x)

        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('Multinomial Distribution')
        plt.title('Multinomial Distribution')
        plt.grid(True)
        plt.show()
  
class DataAnalyzer:
    def __init__(self):
        self.coefficients = []

    def read_data(self):
        coefficient_str = input("Enter the coefficients of the polynomial (separated by spaces): ")
        coefficients = coefficient_str.split()
        self.coefficients = [float(c) for c in coefficients]
 


# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def banner():
    print("""
        
*******************************************************************************************************
*                  (:                 ***   Welcome   ***                     :)                      *
*                                                                                                     *
*    You can use this program to calculate the (Multinomial Distribution) and (display its Graph).    *
*                                Just enter your list of numbers.                                     *                
*                                                                                                     *
*    for example:                                                                                     *
*                 Enter the coefficients of the polynomial (separated by spaces): -1 0 1              *
*                                                                                                     *
*******************************************************************************************************

    """) 

def main():
    banner()
    analyzer = DataAnalyzer()
    analyzer.read_data()
    distribution = MultinomialDistribution(analyzer.coefficients)
    distribution.plot((-10, 10))
    print("*******************************************************************\n")


if __name__ == '__main__':
    main()


# An example of how to use the program is shown.


# Note:
#      To use the full implementation of the Multinomial distribution formula [Type 2], do the following steps:
#           1. See line (31).
#           2. Uncomment the code.
#           3. Comment the [Type 1] in line (21).