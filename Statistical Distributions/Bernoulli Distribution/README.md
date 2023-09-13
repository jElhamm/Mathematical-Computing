# Poisson Distribution Calculator and Graph Plotter

   This program calculates the [*Bernoulli Distribution*](https://en.wikipedia.org/wiki/Bernoulli_distribution) and displays its graph.

## Introduction

   The *Bernoulli distribution* is a discrete probability distribution that models the probability of a binary outcome,
   where the outcome can take only two possible values (usually labeled as success and failure, or 1 and 0).
   In the Bernoulli distribution, there is a single parameter, denoted as 'p', which represents the probability of success.
   The Bernoulli distribution is widely used in various fields, such as statistics, probability theory, and binary data analysis, 
   to model situations with binary outcomes or events with two possible outcomes. It serves as the basis for more complex distributions, 
   such as the binomial distribution and the geometric distribution.
   [*More Information*](https://www.cuemath.com/data/bernoulli-distribution/)

                                     __________________________________________________________________________
                                    |                                                                          |
                                    |       The Bernoulli Distribution Probability Mass Function (PMF):        |
                                    |                                                                          |
                                    |                    PMF(x) = p^x * (1 - p)^(1 - x)                        |
                                    |                                                                          |
                                    |          - p   = probability of success                                  |
                                    |          - 𝑥: 0 or 1 (the possible values in the distribution)           |
                                    |                                                                          |
                                    |__________________________________________________________________________|


## Installation

   1. Clone the repository or download the code files.
   2. Make sure you have **NumPy** and **Matplotlib** installed. If not, you can install them using pip:

                                                ___________________________________________________
                                                |                                                  |                                                        
                                                |     ***      pip install math           ***      |
                                                |     ***      pip install matplotlib     ***      |
                                                |__________________________________________________|

## Usage

   1. Run the program.
   2. Enter a list of numbers, separated by commas. The values should be either (0 or 1), representing failure and success, respectively.
   3. The program will calculate the average of the input data and display it.
   4. The program will generate a graph of the Bernoulli Distribution based on the input data.

## Example

                                **********************************************************************************                                          
                                *             (:               ***   Welcome   ***                 :)            *
                                *                                                                                *
                                *                 You can use this program to calculate the                      *
                                *              (Bernoulli Distribution) and display its Graph.                   *
                                *                                                                                *
                                **********************************************************************************
                                *                                                                                *
                                *         The Bernoulli Distribution Probability Mass Function (PMF):            *
                                *                    PMF(x) = p^x * (1 - p)^(1 - x)                              *
                                *                                                                                *
                                *          --->   x   = 0 or 1 (the possible values in the distribution)         *
                                *          --->   p   = probability of success                                   *
                                *                                                                                *
                                **********************************************************************************

                                Enter a list of numbers (comma-separated), (All values must be either 0 or 1): 0, 1, 0, 1, 1
                                Average: 0.6
              
                               ---> *(The program will display the Poisson Distribution graph based on the entered numbers.)*  <--- 

## License

   * [NumPy](https://numpy.org/)
   * [Matplotlib](https://matplotlib.org/)