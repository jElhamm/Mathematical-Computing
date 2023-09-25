# Gamma Distribution Calculator and Graph Plotter

   This program is a Python implementation of the [*Gamma Distribution*](https://en.wikipedia.org/wiki/Gamma_distribution) calculator and graph plotter. 

## Introduction

   The *Gamma Distribution* is a continuous probability distribution that is commonly used to model the waiting time for a certain number of events to occur in a Poisson process. It is also used to model the sum of squared random variables, such as the sum of squared errors in a linear regression model. The Gamma Distribution has two parameters: shape parameter (k) and scale parameter (θ), which is equal to the mean divided by k. The Gamma Distribution is a generalization of the Exponential Distribution and the Chi-Square Distribution.
   [*More Information*](https://www.probabilitycourse.com/chapter4/4_2_4_Gamma_distribution.php)

                           ______________________________________________________________________________________
                          |                                                                                      |
                          |          Gamma Distribution formula in mathematics is written as follows:            | 
                          |                          f(x) = (x^(k-1) * e^(-x/θ)) / (θ^k * Γ(k))                  |
                          |                                                                                      |
                          |       -  'x' is the random variable                                                  |
                          |       -  'k' is the shape parameter                                                  |
                          |       -  'θ' is the scale parameter, which is equal to the mean divided by k         |
                          |       -  'e' is the base of the natural logarithm                                    |
                          |       -  'Γ' is the gamma function, which is a generalization of the factorial       |
                          |              function to non-integer values.                                         |
                          |______________________________________________________________________________________|

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
   2. Enter a list of numbers separated by commas when prompted.
   3. Enter the shape parameter 'k'.
   4. The program will calculate the mean of the data and display it.
   5. The program will display the Gamma Distribution graph.

## Example

        ******************************************************************************************************************************
        *                                (:               ***   Welcome   ***                 :)                                     *
        *                                                                                                                            *
        *                  You can use this program to calculate the (Gamma Distribution) and display its Graph.                     *
        *                                                                                                                            *
        ******************************************************************************************************************************
        *       Gamma Distribution formula in mathematics is written as follows:   f(x) = (x^(k-1) * e^(-x/θ)) / (θ^k * Γ(k))        *
        *                                                                                                                            *
        *          --->  'x' is the random variable                                                                                  *
        *          --->  'k' is the shape parameter                                                                                  *
        *          --->  'θ' is the scale parameter, which is equal to the mean divided by k                                         *
        *          --->  'e' is the base of the natural logarithm                                                                    *
        *          --->  'Γ' is the gamma function, which is a generalization of the factorial function to non-integer values.       *
        *                                                                                                                            *
        ******************************************************************************************************************************

        ---> Enter a list of numbers (comma-separated): 1,2,3,4,5,6,7,8,9,10
        ---> Enter the shape parameter (k): 2
        ---> Mean: 5.5
              
        * The program will then display the graph of the Gamma Distribution based on the data entered. *

## Note

   This project can be implemented with the (Scipy library). For more information, you can read the following sections:

   * [SciPy](https://scipy.org/)
   * [Install Scipy](https://pypi.org/project/scipy/)
   * [Python Scipy Gamma](https://pythonguides.com/python-scipy-gamma/)

## License

   * [NumPy](https://numpy.org/)
   * [Matplotlib](https://matplotlib.org/)