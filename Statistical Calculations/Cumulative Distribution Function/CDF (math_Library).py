# You can use the program to calculate the (Cumulative Distribution Function).

# Cumulative Distribution Function (CDF) Formula:
# The probability that a random variable X takes on a value less than or equal to a specific value x is calculated as:
# F(x) = Number of values <= x / Total number of values



import math

class CumulativeDistributionFunction:
    def __init__(self, data):
        self.data = data

    # Calculations
    def calculate_cdf(self):
        n = len(self.data)
        cdf = {}
        sorted_data = sorted(self.data)
        cumulative_prob = 0
        for i, value in enumerate(sorted_data):
            cumulative_prob += 1 / n
            cdf[value] = cumulative_prob
        return cdf

    def print_cdf(self):
        cdf = self.calculate_cdf()
        print("   ---> Cumulative Distribution Function (CDF):")
        for value, prob in cdf.items():
            print(f"      - F({value}) = {prob}")
 