# You can use this program to calculate the (Normal Distribution) and (display its Graph).

# Normal Distribution formula in mathematics is written as follows:
#  𝑦 = (1/(𝑠𝑡𝑑 * √(2𝜋))) * 𝑒^−(0.5 * ((𝑥−𝑚𝑒𝑎𝑛)/𝑠𝑡𝑑)^2)    --->  x = input value
#                                                        --->  mean = standard deviation of the data 
#                                                        --->  𝑠𝑡𝑑 = represents the total number of values in the dataset.
#                                                        --->  𝜋 = mathematical constant pi
#                                                        --->  𝑒 = mathematical constant Euler's number


import numpy as np
import matplotlib.pyplot as plt

class NormalDistribution:
    def __init__(self, data):
        self.data = data
        self.mean = np.mean(data)
        self.std = np.std(data)
 
    def plot(self):
        x = np.linspace(min(self.data), max(self.data), 100)                                   # Generate x-values for the plot
        y = (1/(self.std * np.sqrt(2*np.pi))) * np.exp(-0.5*((x-self.mean)/self.std)**2)       # Compute y-values for the normal distribution curve

        plt.plot(x, y)                                                                         # Plot the normal distribution curve
        plt.xlabel('Values')
        plt.ylabel('Probability Density')
        plt.title('Normal Distribution (mean={}, std={})'.format(self.mean, self.std))         # Add title to the plot with mean and standard deviation values
        plt.grid(True)                                                                         # Display grid lines
        plt.show()
  
class DataAnalyzer:
    def __init__(self):
        self.data = []

    def read_data(self):
        data_input = input("Enter a list of numbers (comma-separated): ")
        self.data = [float(x) for x in data_input.split(',')]
        
    # Calculations
    def calculate_statistics(self):
        mean = np.mean(self.data)
        std = np.std(self.data)
        print("Average:", mean)
        print("Standard Deviation:", std)
        return mean, std
 

# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def  banner():
    print("""
        
************************************************************************************
*          (:                 ***   Welcome   ***                     :)           *
*                                                                                  *
*                  You can use this program to calculate the                       *
*                (Normal Distribution) and (display its Graph).                    *
*                      Just enter your list of numbers.                            *
*                                                                                  *
************************************************************************************
*             The formula for Normal Distribution is as follows:                   * 
*             𝑦 = (1/(𝑠𝑡𝑑 * √(2𝜋))) * 𝑒^−(0.5 * ((𝑥−𝑚𝑒𝑎𝑛)/𝑠𝑡𝑑)^2)                  *
*                                                                                  *
*             ***  x    = input value                                              *
*             ***  mean = standard deviation of the data                           *
*             ***  𝑠𝑡𝑑  = represents the total number of values in the dataset.     *
*             ***  𝜋    = mathematical constant pi                                 *
*             ***  𝑒    = mathematical constant Euler's number                     * 
*                                                                                  *
************************************************************************************
    """)  

def main():
    banner()
    analyzer = DataAnalyzer()
    analyzer.read_data()
    mean, std = analyzer.calculate_statistics()
    plotter = NormalDistribution(analyzer.data)
    plotter.plot()

if __name__ == '__main__':
    main()

# An example of how to use the program is shown.