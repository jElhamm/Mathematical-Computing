# Laplace Transform Of Matrix

   You can use this program to calculate the [(Laplace transform)](https://en.wikipedia.org/wiki/Laplace_transform) of a *numerical matrix*.

## What is the Laplace Transform?

                    ____________________________________________________________________________________________
                    |                                                                                           |
                    |                Consider f(t) as a function of the independent variable t.                 |
                    |           The Laplace transform of f(t), denoted as F(s), is a function of a              |
                    |      new variable s, which can generally be complex. The variable s must be numeric.      |
                    |___________________________________________________________________________________________|

## Usage

   1. Run the program.
   2. Enter the number of rows and columns for the matrix.
   3. Enter the elements of the matrix.
   4. Enter the value of (s).
   5. The program will calculate the Laplace transform of each element in the matrix.
   6. The *transformed matrix* will be displayed as the output.

## Example

   Let's consider an example to understand how the program works.

   * Suppose we have a 2x2 matrix A as follows:

                                                A = [[ 2.0 , 4.0 ],
                                                     [ 6.0 , 8.0 ]]

   * We want to calculate the Laplace transform of each element in A for a specific value of s.
   [Let's say the value of s is 3].

   * The transformed matrix will be:

                                                Transformed Matrix = [[ 0.4 , 0.8 ],
                                                                      [ 1.2 , 1.6 ]]

## Notes

   * The Laplace transform is applied to each element in the matrix individually.
   * The program supports matrices of any size.
   * The program requires the input of the value of (s).
   * To use the    [  *np.zeros((self.rows, self.columns))*  ]    method in line 25, you need to import the [numpy library](https://numpy.org/).

## References

   * [numpy](https://pypi.org/project/numpy/)
   * [numpy.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html)
   * [Laplace transform](https://en.wikipedia.org/wiki/Laplace_transform)
   * [Laplace transform](https://www.khanacademy.org/math/differential-equations/laplace-transform)

________________________________________________________________________________________________________________________________________

   *(Feel free to modify and use the program according to your needs.)*