# You can use this program to calculate the (Uniform Distribution) and (display its Graph).

# Uniform Distribution formula in mathematics is written as follows:        𝑦 = 1 / (𝑏 - 𝑎)
#                                                                     --->  𝑦 = probability density function
#                                                                     --->  𝑎 = minimum value
#                                                                     --->  𝑏 = maximum value



import numpy as np
import matplotlib.pyplot as plt

class UniformDistribution:
    def __init__(self, data):
        self.data = data

    def plot(self):
        min_value = min(self.data)
        max_value = max(self.data)
        probability = 1 / (max_value - min_value)

        x = np.linspace(min_value, max_value, 100)
        y = np.full_like(x, probability)

        plt.plot(x, y)
        plt.xlabel('Values')
        plt.ylabel('Probability Density Function')
        plt.title('Uniform Distribution')
        plt.grid(True)
        plt.show()
 
class DataAnalyzer:
    def __init__(self):
        self.data = []

    def read_data(self):
        data_input = input("---> Enter a list of numbers (comma-separated): ")
        self.data = [float(x.strip()) for x in data_input.split(',')]

    def calculate_statistics(self):
        mean = np.mean(self.data)
        print("---> Mean:", mean)
        return mean
 

# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def banner():
    print("""
        
************************************************************************************
*          (:                 ***   Welcome   ***                     :)           *
*                                                                                  *
*                  You can use this program to calculate the                       *
*                (Uniform Distribution) and (display its Graph).                   *
*                      Just enter your list of numbers.                            *
*                                                                                  *
************************************************************************************
*       The formula for Uniform Distribution (Probability Density Function):       * 
*                     𝑦    = 1 / (𝑏 - 𝑎)                                           *
*                   - 𝑦    = probability density function                          *
*                   - 𝑎    = minimum value                                         *
*                   - 𝑏    = maximum value                                         *
*                                                                                  *
************************************************************************************
    """)

def main():
    banner()
    analyzer = DataAnalyzer()
    analyzer.read_data()
    mean = analyzer.calculate_statistics()
    plotter = UniformDistribution(analyzer.data)
    plotter.plot()
    print("*********************************************************************\n")


if __name__ == '__main__':
    main()


# An example of how to use the program is shown.
 

# Note:
#      - In the code, we specify the minimum and maximum values ​​according to the input data provided by the user. 
#      - Then we determine the probability of a uniform distribution between these two values. 
#      - Finally, using matplotlib, we draw a horizontal line with constant probability density in this interval.