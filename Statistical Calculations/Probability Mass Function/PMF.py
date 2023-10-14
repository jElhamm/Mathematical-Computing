# You can use the program to calculate the (Probability Mass Function).

# The formula used to calculate the Probability Mass Function (PMF) is as follows:
       
#           PMF = Count of each value / Total number of values



import collections

class ProbabilityMassFunction:
    def __init__(self, data):
        self.data = data

    # Calculation
    def calculate_pmf(self):
        counter = collections.Counter(self.data)
        n = len(self.data)
        pmf = {x: count / n for x, count in counter.items()}
        return pmf

    def print_pmf(self):
        pmf = self.calculate_pmf()
        print("   ---> Probability Mass Function (PMF):")
        for value, probability in pmf.items():
            print(f"        {value}: {probability}")
 