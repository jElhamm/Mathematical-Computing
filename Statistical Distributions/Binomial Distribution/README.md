# Calculating the Binomial Distribution and Displaying its Graph

   This program allows you to calculate the probability mass function (PMF) and display the graph of a [*Binomial Distribution*](https://en.wikipedia.org/wiki/Binomial_distribution). 
   The binomial distribution is a discrete probability distribution that models the number of successes in a fixed number of independent Bernoulli trials.

## Introduction

   The *Binomial Distribution* is a probability distribution that models the number of successes in a fixed number of independent trials. It is defined by the probability of success in each trial (denoted as 'p') and the total number of trials (denoted as 'n'). The probability mass function (PMF) of the Binomial Distribution calculates the probability of obtaining a specific number of successes (denoted as 'k') in the given number of trials.
   [*More Information*](https://www.statisticshowto.com/probability-and-statistics/binomial-theorem/binomial-distribution-formula/)

                   _________________________________________________________________________________________________
                  |                                                                                                 |
                  |       Binomial Distribution formula in mathematics is written as follows:                       |
                  |                                                                                                 |
                  |                 PMF(k) = C(n, k) * p^k * (1 - p)^(n - k)                                        |
                  |                                                                                                 |
                  |       - PMF(k)  : probability of obtaining 'k' successes in a binomial distribution.            |
                  |       - C(n, k) : binomial coefficient, calculated as n! / (k! * (n - k)!), which               |
                  |                   represents the number of ways to choose 'k' successes from 'n' trials.        |
                  |       - p       : probability of success for each trial.                                        |
                  |       - n       : total number of trials.                                                       |
                  |_________________________________________________________________________________________________|


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
   2. Enter the number of trials (n) when prompted.
   3. Enter the probability of success (p) when prompted. Note that p must be between 0 and 1.
   4.The program will calculate the average and display it.
   5. A bar graph representing the binomial distribution will be shown.

## Example

                  **************************************************************************************************                
                  *                  (:               ***   Welcome   ***                 :)                       *
                  *                                                                                                *                
                  *    You can use this program to calculate the (Binomial Distribution) and display its Graph.    *
                  *                                                                                                *
                  **************************************************************************************************
                  *                                                                                                *
                  *         Binomial Distribution formula in mathematics is written as follows:                    *
                  *                                                                                                *
                  *                    PMF(k) = C(n, k) * p^k * (1 - p)^(n - k)                                    *
                  *                                                                                                *
                  *  --->  PMF(k)  = probability of obtaining 'k' successes in a binomial distribution.            *
                  *  --->  C(n, k) = binomial coefficient, calculated as n! / (k! * (n - k)!), which               *
                  *                  represents the number of ways to choose 'k' successes from 'n' trials.        *
                  *                                                                                                *
                  *  --->  p       = probability of success for each trial.                                        *
                  *  --->  n       = total number of trials.                                                       *
                  *                                                                                                *
                  **************************************************************************************************

                  ---> Enter the number of trials (n): 10
                  ---> Enter the probability of success (p): 0.4
                  ---> Average: 4.0

                  After entering the input values, the program will display the 
                  average and show a bar graph visualizing the binomial distribution.

## License

   * [math](https://docs.python.org/3/library/math.html)
   * [NumPy](https://numpy.org/)
   * [Matplotlib](https://matplotlib.org/)
   * [Binomial Distribution](https://www.w3schools.com/python/numpy/numpy_random_binomial.asp)
   * [Python - Binomial Distribution](https://www.geeksforgeeks.org/python-binomial-distribution/)