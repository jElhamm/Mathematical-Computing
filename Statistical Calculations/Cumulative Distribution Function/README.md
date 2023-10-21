# Cumulative Distribution Function (CDF)

   This folder contains two Python programs that calculate the [*Cumulative Distribution Function*](https://en.wikipedia.org/wiki/Cumulative_distribution_function) of a dataset. 
   Both programs use different libraries for Cumulative Distribution Function calculation.

   * [Program 1](CDF%20(math_Library).py) --->    [math Library](https://docs.python.org/3/library/math.html)
   * [Program 2](CDF%20(numpy_Library).py) --->    [numpy Library](https://numpy.org/)

## Description

    A Cumulative Distribution Function (CDF) is a concept in probability theory and statistics. It is used to describe the probability distribution of a random variable. The CDF provides information about the probability that a random variable takes on a value less than or equal to a given value.

    Mathematically, for a random variable X, the CDF is denoted as F(x) and is defined as:              F(x) = P(X ≤ x)

    In words, F(x) represents the probability that the random variable X takes on a value less than or equal to x. The CDF is a monotonically increasing function, meaning it starts at 0 and approaches 1 as x increases.

    The CDF is valuable in various statistical analyses, such as calculating percentiles, determining the likelihood of certain events, and deriving other statistical measures like median and interquartile range.
   [*More Information*](http://amsi.org.au/ESA_Senior_Years/SeniorTopic4/4e/4e_2content_2.html)

## Usage

   1. Run the program.
   2. You will be prompted to enter a list of data, separated by spaces.
   3. Input the desired data points.
   4. The program calculates and displays the Cumulative Distribution Function.

   * *Both programs are included in this repository, with separate files for each.*

## References

   * [How to calculate and plot a Cumulative Distribution function with Matplotlib in Python?](https://www.geeksforgeeks.org/how-to-calculate-and-plot-a-cumulative-distribution-function-with-matplotlib-in-python/)