# Exponential Distribution Calculator and Graph Plotter

   This program is a Python implementation of the [*Laplacian Distribution*](https://en.wikipedia.org/wiki/Laplace_distribution) calculator and graph plotter. 
   The Laplacian Distribution is a probability distribution that is used to model data with heavy tails or outliers. 
   The program takes a list of numbers as input, calculates the scale parameter and location parameter of the Laplacian Distribution, 
   and then plots the probability density function of the distribution.

## Introduction

   The *Laplacian Distribution* is a probability distribution that is used to model data with sharp peaks and heavy tails. It is a continuous probability distribution that is similar to the Gaussian distribution, but has a sharper peak and heavier tails. The Laplacian distribution is also known as the double exponential distribution because it has two exponential tails. The scale parameter of the Laplacian distribution is calculated as the square root of 0.5 times the second moment of the data. The Laplacian distribution is used in a variety of applications, including image processing, computer vision, and machine learning. It is particularly useful for edge detection and image enhancement because it can effectively preserve edges while smoothing out noise.

                           ______________________________________________________________________________________
                          |                                                                                      |
                          |          Laplacian Distribution formula in mathematics is written as follows:        | 
                          |                           f(x) = 0.5 * e^(-|x - μ| / b) / b                          |
                          |                                                                                      |
                          |       -  μ    = location parameter                                                   |
                          |       -  b    = scale parameter                                                      |
                          |       -  The scale parameter is calculated as the square root of 0.5 times the       |
                          |          median absolute deviation of the data from the median.                      |
                          |______________________________________________________________________________________|

## Installation

   1. Clone the repository or download the code files.
   2. Make sure you have **NumPy** and **Matplotlib** installed. If not, you can install them using pip:

                                         __________________________________________________
                                        |                                                  |
                                        |     ***      pip install numpy          ***      |
                                        |     ***      pip install matplotlib     ***      |
                                        |__________________________________________________|

## Usage

   1. Run the program.
   2. Enter a list of numbers separated by commas when prompted.
   3. The program will calculate the mean of the data and display it.
   4. The program will then plot the probability density function of the Laplacian Distribution.

## Example

                    ****************************************************************************************************
                    *                  (:               ***   Welcome   ***                 :)                         *
                    *                                                                                                  *
                    *    You can use this program to calculate the (Laplacian Distribution) and display its Graph.     *
                    *                                                                                                  *
                    ****************************************************************************************************
                    *                                                                                                  *
                    *           Laplacian Distribution formula in mathematics is written as follows:                   *
                    *                                                                                                  *
                    *                             f(x) = 0.5 * e^(-|x - μ| / b) / b                                    *
                    *                                                                                                  *
                    *                  ---> μ    = location parameter                                                  *
                    *                  ---> b    = scale parameter                                                     *
                    *                                                                                                  *
                    *          The scale parameter is calculated as the square root of 0.5 times the                   *
                    *                 median absolute deviation of the data from the median.                           *
                    *                                                                                                  *
                    ****************************************************************************************************

                    ---> Enter a list of numbers (comma-separated): 1,2,3,4,5,6,7,8,9,10
                    ---> Mean: 5.5
              
                    * The program will then display the graph of the Laplacian Distribution based on the data entered. *

## License

   * [NumPy](https://numpy.org/)
   * [Matplotlib](https://matplotlib.org/)
   * [Python – Laplace Distribution in Statistics](https://www.geeksforgeeks.org/python-laplace-distribution-in-statistics/)