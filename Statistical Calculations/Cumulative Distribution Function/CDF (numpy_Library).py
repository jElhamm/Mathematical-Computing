# You can use the program to calculate the (Cumulative Distribution Function).

# Cumulative Distribution Function (CDF) Formula:
# The probability that a random variable X takes on a value less than or equal to a specific value x is calculated as:
# F(x) = Number of values <= x / Total number of values



import numpy as np

class CumulativeDistributionFunction:
    def __init__(self, data):
        self.data = data

    # Calculations
    def calculate_cdf(self):
        sorted_data = np.sort(self.data)
        n = len(sorted_data)
        cdf = np.arange(1, n + 1) / n
        return dict(zip(sorted_data, cdf))

    def print_cdf(self):
        cdf = self.calculate_cdf()
        print("   ---> Cumulative Distribution Function (CDF):")
        for value, prob in cdf.items():
            print(f"      - F({value}) = {prob}")
 


# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def banner():
    print("""
        
################################################################################
#                             (:   Welcome   :)                                #
#                                                                              #
#      You can use the program to calculate the Cumulative Distribution        #
#      Function (CDF).                                                         #
#                                                                              #
#      The Cumulative Distribution Function (CDF) calculates                   #
#      the probability that a random variable X takes on a value less than     #
#      or equal to a specific value x.                                         #
#                                                                              #
################################################################################
    """)

def main():
    banner()
    data = input("   ---> Enter a list of data (separated by spaces): ").split()
    data = [float(x) for x in data]
    cdf_calculator = CumulativeDistributionFunction(data)
    print("\n**********************************************************************************")
    cdf_calculator.print_cdf()
    print("**********************************************************************************\n")

if __name__ == "__main__":
    main()


# An example of how to use the program is shown.