# You can use the program to calculate the (Probability Mass Function).

# The formula used to calculate the Probability Mass Function (PMF) is as follows:
       
#           PMF = Count of each value / Total number of values



import math

class ProbabilityMassFunction:
    def __init__(self, data):
        self.data = data

    # Calculations
    def calculate_pmf(self):
        n = len(self.data)
        pmf = {}
        for value in set(self.data):
            count = self.data.count(value)
            pmf[value] = count / n
        return pmf

    def print_pmf(self):
        pmf = self.calculate_pmf()
        print("   ---> Probability Mass Function (PMF):")
        for value, prob in pmf.items():
            print(f"      - P({value}) = {prob}")
 