# Poisson Distribution Calculator and Graph Plotter

   This program calculates the [*Poisson Distribution*](https://en.wikipedia.org/wiki/Poisson_distribution) for a given set of numbers and displays its graph.


## Introduction

   The *Poisson Distribution* is a probability distribution that represents the number of events occurring
   in a fixed interval of time or space, given a known average rate of occurrence. 
   This program allows you to calculate the Poisson Distribution and visualize it as a graph.
   [*More Information*](https://www.scribbr.com/statistics/poisson-distribution/)

             _______________________________________________________________________________________
            |                                                                                       |
            |                The formula for the Poisson Distribution is as follows:                |
            |                                                                                       |
            |                                𝑦 = (𝑒^−𝜆 * 𝜆^𝑥) / 𝑥!                                  |
            |                                                                                       |
            |           - 𝑦: Probability mass function                                              |
            |           - 𝑥: Input value                                                            |
            |           - 𝜆: Mean or average rate of the event                                      |
            |           - 𝑒: Mathematical constant Euler's number (approximately 2.71828)           |   
            |           - 𝑥!: Factorial of 𝑥                                                        |
            |_______________________________________________________________________________________|


## Installation

   1. Clone the repository or download the code files.
   2. Make sure you have **NumPy** , **Matplotlib** and **Math** installed. If not, you can install them using pip:

                        ___________________________________________________
                        |                                                  |
                        |     ***      pip install math           ***      |
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

              Enter a list of numbers (comma-separated): 1,2,3,4,5
              Average: 3.0
              
              ---> *(The program will display the Poisson Distribution graph based on the entered numbers.)*  <--- 

## License

   * [NumPy](https://numpy.org/)
   * [Matplotlib](https://matplotlib.org/)
   * [NumPy Poisson Distribution](https://www.alphacodingskills.com/numpy/numpy-poisson-distribution.php)
   * [Plot a poisson distribution graph in python](https://stackoverflow.com/questions/51242748/plot-a-poisson-distribution-graph-in-python)