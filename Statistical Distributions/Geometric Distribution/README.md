# Geometric Distribution Calculator and Graph Plotter

   This program allows you to calculate the [*Geometric Distribution*](https://en.wikipedia.org/wiki/Geometric_distribution) and display its graph based on a given list of numbers.

## Introduction

   The *Geometric Distribution* is a probability distribution that models the number of trials needed 
   to achieve the first success in a sequence of independent Bernoulli trials. It is often used to analyze 
   scenarios where repeated experiments are conducted until a desired outcome (success) occurs for the first time.

   In the Geometric Distribution, the probability of success (usually denoted as 'p') remains constant for each trial. 
   The probability mass function gives the probability of achieving the first success at a specific trial ('x').
   [*more information*](https://www.britannica.com/topic/geometric-distribution)

                     _______________________________________________________________________
                    |                                                                       |
                    |         The formula for Geometric Distribution is as follows:         | 
                    |                       𝑦 = (1-𝑝)^(𝑥-1) * 𝑝                             |
                    |                                                                       |
                    |                 -  𝑦    = probability mass function                   |
                    |                 -  𝑥    = input value                                 |
                    |                 -  𝑝    = probability parameter                       |
                    |_______________________________________________________________________|


    * The Geometric Distribution is commonly used in various fields such as statistics, probability theory, 
    and reliability analysis. It provides insights into the expected waiting time or number of trials until 
    a success occurs in a sequence of independent trials.

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
   2. Enter a list of numbers (comma-separated) when prompted.
   3. The program will calculate the average of the entered numbers.
   4. It will then generate the Poisson Distribution graph and display it.

## Example

                    ************************************************************************************
                    *          (:                 ***   Welcome   ***                     :)           *
                    *                                                                                  *
                    *                  You can use this program to calculate the                       *
                    *                (Poisson Distribution) and (display its Graph).                   *
                    *                      Just enter your list of numbers.                            *
                    *                                                                                  *
                    ************************************************************************************
                    *             The formula for Poisson Distribution is as follows:                  * 
                    *                          𝑦 = (𝑒^−𝜆 * 𝜆^𝑥) / 𝑥!                                   *
                    *                                                                                  *
                    *              **  𝑦    = probability mass function                                *
                    *              **  𝑥    = input value                                              *
                    *              **  𝜆    = mean or average rate of the event                        *
                    *              **  𝑒    = mathematical constant Euler's number                     * 
                    *              **  𝑥!   = factorial of x                                           *
                    *                                                                                  *
                    ************************************************************************************

                    ---> Enter a list of numbers (comma-separated): 1,2,3,4,5
                         Average: 3.0
              
            ---> *(The program will display the Geometric Distribution graph based on the entered numbers.)*  <--- 

## License

   * [NumPy](https://numpy.org/)
   * [Matplotlib](https://matplotlib.org/)
   * [NumPy Geometric Distribution](https://www.alphacodingskills.com/numpy/numpy-geometric-distribution.php)