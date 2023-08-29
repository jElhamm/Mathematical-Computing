# Covariance

   This folder contains two Python programs that calculate the [*Covariance*](https://en.wikipedia.org/wiki/Covariance) of a dataset. 
   Both programs use different libraries for Covariance calculation.

   * [Program 1](covariance%20(math_library).py) --->    [math Library](https://docs.python.org/3/library/math.html)
   * [Program 2](covariance%20(statistics_library).py) --->    [statistics Library](https://docs.python.org/3/library/statistics.html)

## Description

   Covariance is a statistical measure that helps us understand the relationship between two random variables. 
   It measures how changes in one variable correspond to changes in another variable. In simple terms, it indicates
   the degree to which the variables move together. A positive covariance means that the variables tend to move in the 
   same direction, while a negative covariance indicates they move in opposite directions. Covariance provides important information when analyzing the dependence and potential correlation between variables.
   [*More Information*](https://byjus.com/maths/covariance/)

                  __________________________________________________________________________________
                  |                                                                                 |
                  |                 The formula for covariance is as follows:                       |
                  |                ___________________________________________                      |
                  |               |                                           |                     |
                  |               |   Cov(x, y) = ∑((xᵢ - μₓ)(yᵢ - μᵧ)) / N   |                     |
                  |               |___________________________________________|                     |
                  |                                                                                 |
                  |       --->   Cov(x, y) = represents covariance between the datasets             |
                  |       --->   Σ = sum of                                                         |
                  |       --->   xi = represents each individual value in the first dataset         |
                  |       --->   yi = represents each individual value in the second dataset        |
                  |       --->   μₓ = represents the mean of the first dataset                      |
                  |       --->   μᵧ = represents the mean of the second dataset                     |
                  |       --->   N = represents the total number of values in the datasets          |
                  |_________________________________________________________________________________|



## Usage

   1. Run the program.
   2. You will be prompted to enter a list of data, separated by spaces.
   3. Input the desired data points.
   4. The program calculates and displays the covariance.

   * *Both programs are included in this repository, with separate files for each.*

## References

   * [Mathematical functions](https://docs.python.org/3/library/math.html)
   * [Mathematical statistics functions](https://docs.python.org/3/library/statistics.html)
   * [Covariance and Correlation in Python](https://stackabuse.com/covariance-and-correlation-in-python/)