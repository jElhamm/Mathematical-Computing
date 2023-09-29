# n-th Order Moment
 
   This Python program calculates the [*n-th Order Moment*](https://en.wikipedia.org/wiki/Moment_(mathematics)) of a given dataset. The n-th Order Moment is a mathematical formula used to measure the concentration or distribution of data.
   Both programs use different libraries for variance calculation.

   * [Program 1](moment%20(math_library).py) --->    [math Library](https://docs.python.org/3/library/math.html)
   * [Program 2](moment%20(statistics_library).py) --->    [statistics Library](https://docs.python.org/3/library/statistics.html)

## Description

   The n-th order moment is a statistical concept used to describe the distribution and properties of a set of data. 
   It involves calculating the average value of the data raised to the power of n. The order of the moment determines the level 
   of emphasis on different aspects of the data's distribution, such as its central tendency or dispersion. Positive moments indicate a 
   concentration of data around the mean, while negative moments suggest data points dispersed away from the mean.


                         ________________________________________________________________________________
                        |                                                                                |
                        |              The formula for (n_th Order Moment) is as follows:                |
                        |                          (1/N) * Σ((xi - mean)^n)                              |
                        |                                                                                |
                        |        --->    N = is the number of data points in the dataset                 |
                        |        --->    Σ   = sum of                                                    |
                        |        --->    xi  = is the ith data point                                     |
                        |        --->    mean   = is the mean of the dataset                             |
                        |        --->    n   = is the order of the moment                                |
                        |________________________________________________________________________________|


## Usage

   1. Run the program.
   2. Enter a list of data points separated by spaces when prompted.
   3. Enter the desired order of the moment.
   4. The program will calculate and display the n-th Order Moment.

   * *Both programs are included in this repository, with separate files for each.*

## References

   * [Python statistics Module](https://www.w3schools.com/python/module_statistics.asp)
   * [Moments and Moment Generating Functions](http://www.milefoot.com/math/stat/rv-moments.htm)