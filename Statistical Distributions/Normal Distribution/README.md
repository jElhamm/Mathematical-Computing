# Normal Distribution Calculator and Graph Plotter

   This program calculates the [*Normal Distribution*](https://en.wikipedia.org/wiki/Normal_distribution) and [*Displays its Graph*](https://en.wikipedia.org/wiki/Normal_probability_plot) based on a given set of numbers. 
   It uses the formula for the Normal Distributionn in mathematics.

## Normal Distribution

   The normal distribution, also known as the Gaussian distribution, is a probability distribution that is symmetric and bell-shaped. It is often used in statistics and data analysis to describe random variables and phenomena that tend to cluster around a central value.

   In a normal distribution, the majority of data points are concentrated around the mean (the central value) and gradually decrease as they move away from the mean. The distribution is characterized by two parameters: the mean and the standard deviation.
   [*More Information*](https://www.scribbr.com/statistics/normal-distribution/#:~:text=In%20a%20normal%20distribution%2C%20data%20are%20symmetrically%20distributed%20with%20no,same%20in%20a%20normal%20distribution.)

                 _____________________________________________________________________________
                |                                                                             |
                |              The Normal Distribution formula is given as:                   |
                |                                                                             |
                |           𝑦 = (1/(𝑠𝑡𝑑 * √(2𝜋))) * 𝑒^−(0.5 * ((𝑥−𝑚𝑒𝑎𝑛)/𝑠𝑡𝑑)^2)               |
                |                                                                             |  
                |             - 𝑥: Input value                                                |
                |             - 𝑚𝑒𝑎𝑛: Mean (standard deviation of the data)                  |
                |             - 𝑠𝑡𝑑: Represents the total number of values in the dataset     |
                |             - 𝜋: Mathematical constant (pi)                                 |
                |             - 𝑒: Mathematical constant Euler's number                       |
                |_____________________________________________________________________________|


## Installation

   1. Clone the repository or download the code files.
   2. Make sure you have **NumPy** and **Matplotlib** installed. If not, you can install them using pip:

                        ___________________________________________________
                        |                                                  |
                        |     ***      pip install numpy          ***      |
                        |     ***      pip install matplotlib     ***      |
                        |__________________________________________________|

## Usage

   1. Run the program.
   2. Enter a list of numbers when prompted. Separate the numbers by commas.
   3. The program will calculate the mean and standard deviation of the input data.
   4. It will then plot the normal distribution graph based on the calculated values.
   5. The graph will be displayed in a separate window.

## Example

            ************************************************************************************
            *          (:                 ***   Welcome   ***                     :)           *
            *                                                                                  *
            *                  You can use this program to calculate the                       *
            *                (Normal Distribution) and (display its Graph).                    *
            *                      Just enter your list of numbers.                            *
            *                                                                                  *
            ************************************************************************************
            *             The formula for Normal Distribution is as follows:                   * 
            *             𝑦 = (1/(𝑠𝑡𝑑 * √(2𝜋))) * 𝑒^−(0.5 * ((𝑥−𝑚𝑒𝑎𝑛)/𝑠𝑡𝑑)^2)                  *
            *                                                                                  *
            *             ***  x    = input value                                              *
            *             ***  mean = standard deviation of the data                           *
            *             ***  𝑠𝑡𝑑  = represents the total number of values in the dataset.     *
            *             ***  𝜋    = mathematical constant pi                                 *
            *             ***  𝑒    = mathematical constant Euler's number                     * 
            *                                                                                  *
            ************************************************************************************

            Enter a list of numbers (comma-separated): 1,2,3,4,5,6,7,8,9,10
            Average: 5.5
            Standard Deviation: 2.8722813232690143

            ---> (Then the normal distribution graph will be displayed.) <---

## License

   * [NumPy](https://numpy.org/)
   * [Matplotlib](https://matplotlib.org/)
   * [numpy.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html)
   * [Normal Distribution Plot using Numpy and Matplotlib](https://www.geeksforgeeks.org/normal-distribution-plot-using-numpy-and-matplotlib/)