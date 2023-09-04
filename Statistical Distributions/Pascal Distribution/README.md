# Pascal Distribution Calculator and Graph Plotter

   This program can be used to calculate the [*Pascal Distribution*](https://en.wikipedia.org/wiki/Negative_binomial_distribution) and display its graph. The Pascal Distribution is a probability distribution that models the number of failures before a certain number of successes occur. It is also known as the Negative Binomial Distribution.


## Introduction

   The *Pascal Distribution*, also known as the *Negative Binomial Distribution*, is a probability distribution that models the number of failures that occur before a certain number of successes are achieved. It is used to analyze scenarios where we are interested in the number of trials needed to get a fixed number of successes.
   [*More Information*](https://vitalflux.com/negative-binomial-distribution-python-examples/)

                 _______________________________________________________________________________________
                |                                                                                       |               
                |             The Pascal Distribution Probability Mass Function (PMF):                  |
                |                                                                                       |
                |                    PMF(x) = C(x + r - 1, x) * p^r * (1 - p)^x                         |
                |                                                                                       |
                |               - C(n, k)   = the binomial coefficient                                  |
                |               - x         = number of failures before the rth success occurs          |
                |               - r         = number of successes                                       |
                |               - p         = probability of success                                    |   
                |_______________________________________________________________________________________|


   * By analyzing the Pascal Distribution, we can understand the likelihood and distribution of the number of trials needed to reach a specific number of successes in various scenarios. This distribution finds applications in areas such as quality control, reliability analysis, and project management.


## Installation

   1. Clone the repository or download the code files.
   2. Make sure you have **NumPy** , **Matplotlib** and **Math** installed. If not, you can install them using pip:

                               __________________________________________________
                              |                                                  |
                              |     ***      pip install math           ***      |
                              |     ***      pip install numpy          ***      |
                              |     ***      pip install matplotlib     ***      |
                              |__________________________________________________|

## Usage

   1. Run the program.
   2. Enter a list of numbers, separated by commas, when prompted.
   3. The program will calculate the Pascal Distribution based on the entered data and display the graph.

## Example

              **************************************************************************************
              *          (:                 ***   Welcome   ***                     :)             *
              *                                                                                    *
              *                  You can use this program to calculate the                         *
              *                (Pascal Distribution) and (display its Graph).                      *
              *                      Just enter your list of numbers.                              *
              *                                                                                    *
              **************************************************************************************
              *             The Pascal Distribution Probability Mass Function (PMF):               * 
              *                    PMF(x) = C(x + r - 1, x) * p^r * (1 - p)^x                      *
              *                                                                                    *
              *              ***  C(n, k)   = the binomial coefficient                             *
              *              ***  x         = number of failures before the rth success occurs     *
              *              ***  r         = number of successes                                  *
              *              ***  p         = probability of success                               *
              *                                                                                    *
              **************************************************************************************

              Enter a list of numbers (comma-separated): 1,2,3,4,5
              Average: 3.0
              
              ---> (The program will display the Poisson Distribution graph based on the entered numbers.)  <--- 

## License

   * [NumPy](https://numpy.org/)
   * [Matplotlib](https://matplotlib.org/)
   * [Binomial coefficient](https://en.wikipedia.org/wiki/Binomial_coefficient)
   * [Python | math.factorial() function](https://www.geeksforgeeks.org/python-math-factorial-function/)