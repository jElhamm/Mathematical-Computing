# Variance
 
   This folder contains two Python programs that calculate the [*Variance*](https://en.wikipedia.org/wiki/Variance) of a dataset. 
   Both programs use different libraries for variance calculation.

   * [Program 1](variance%20(math_library).py) --->    [math Library](https://docs.python.org/3/library/math.html)
   * [Program 2](variance%20(statistics_library).py) --->    [statistics Library](https://docs.python.org/3/library/statistics.html)

## Description

   Variance is a statistical measure that quantifies the dispersion or spread of a set of data points around their mean.
   It measures how far each data point in a set is from the mean and provides an understanding of the average degree to 
   which the data points differ from the mean. A low Variance indicates that the data points are closely clustered around
   the mean, while a high variance suggests that the data points are widely dispersed. 
   Variance is commonly used in finance, physics, and social sciences to analyze and compare the variability of different datasets.
   [*More Information*](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance)


                         ________________________________________________________________________________
                        |                                                                                |
                        |                   The formula for (Variance) is as follows:                    |
                        |                             Var = ∑(xᵢ - μ)² / N                               |
                        |                                                                                |
                        |        --->    Var = represents variance                                       |
                        |        --->    Σ   = sum of                                                    |
                        |        --->    xi  = represents each individual value in the dataset           |
                        |        --->    μ   = represents the mean of the dataset                        |
                        |        --->    N   = represents the total number of values in the dataset      |
                        |________________________________________________________________________________|


## Usage

   1. Run the program.
   2. You will be prompted to enter a list of data, separated by spaces.
   3. Input the desired data points.
   4. The program calculates and displays the variance.

   * *Both programs are included in this repository, with separate files for each.*

## References

   * [Calculating Variance](https://stackabuse.com/calculating-variance-and-standard-deviation-in-python/)
   * [Program for Variance](https://www.geeksforgeeks.org/program-for-variance-and-standard-deviation-of-an-array/)
   * [Python statistics Module](https://www.w3schools.com/python/module_statistics.asp)