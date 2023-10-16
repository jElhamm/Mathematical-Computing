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
 


# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def banner():
    print("""
        
################################################################################
#                              ***   Welcome   ***                             #
#                                                                              #             
#      You can use the program to calculate the Probability Mass Function.     #
#                                                                              #
#            The Probability Mass Function (PMF) calculates the                #
#          probability of each value occurring in the given data set.          #
#                                                                              #    
################################################################################
    """)

def main():
    banner()
    data = input("   ---> Enter a list of data (separated by spaces): ").split()
    data = [float(x) for x in data]
    pmf_calculator = ProbabilityMassFunction(data)
    print("\n**********************************************************************************")
    pmf_calculator.print_pmf()
    print("**********************************************************************************\n")

if __name__ == "__main__":
    main()


# An example of how to use the program is shown. 