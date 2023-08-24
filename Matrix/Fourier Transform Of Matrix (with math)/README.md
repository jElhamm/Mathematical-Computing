# Fourier transform of Matrix

   The [Fourier Transform](https://en.wikipedia.org/wiki/Fourier_transform) is a mathematical technique that transforms a signal from its time domain representation to its frequency domain representation.
   It decomposes a signal into its constituent frequencies, allowing us to analyze and manipulate the different frequency components of the signal.

   The Fourier transform can be applied to various types of signals, including [*continuous-time signals*](https://en.wikipedia.org/wiki/Discrete_time_and_continuous_time), [*discrete-time signals*](https://en.wikipedia.org/wiki/Discrete_time_and_continuous_time), and *two-dimensional signals* like images. In this program, we focus on the 2D Fourier transform, specifically for matrices.


## [Fast Fourier Transform (FFT)](https://en.wikipedia.org/wiki/Fast_Fourier_transform)

                 " The (FFT Algorithm) is a fast and efficient algorithm for calculating the discrete Fourier transform. "
            " It exploits the symmetry and periodicity properties of the Fourier transform to reduce the number of computations. "

            _______________________________________________________________________________________________________________
            |  ST |                                                                                                         |
            |  EP |                 How the       * Fast Fourier Transform (FFT) *       Algorithm works                    |
            |_____|_________________________________________________________________________________________________________|
            |  1  | Check if the number of rows and columns is a power of 2. If not, display an error message and return.   |
            |_____|_________________________________________________________________________________________________________|
            |  2  | Apply the 1D FFT on each row of the matrix.                                                             |
            |_____|_________________________________________________________________________________________________________|
            |  3  | Transpose the matrix.                                                                                   |
            |_____|_________________________________________________________________________________________________________|
            |  4  | Apply the 1D FFT on each column of the transposed matrix.                                               |
            |_____|_________________________________________________________________________________________________________|
            |  5  | Transpose the matrix back to its original form.                                                         |
            |_____|_________________________________________________________________________________________________________|

## 1D FFT

                         " The (1D Fourier Transform Algorithm) is implemented in the fft1D() method."
                " This function is an auxiliary function that we use to calculate the (2D Fourier Transform). "

         ___________________________________________________________________________________________________________________________
        |  ST |                                                                                                                     |
        |  EP |                     How the       * 1D Fast Fourier Transform (FFT) *       Algorithm works                         |
        |_____|_____________________________________________________________________________________________________________________|
        |  1  | If the length of the row is 1 (base case), return the row as it is.                                                 |
        |_____|_____________________________________________________________________________________________________________________|
        |  2  | Split the row into even and odd indexes.                                                                            |
        |_____|_____________________________________________________________________________________________________________________|
        |  3  | Recursively apply the 1D FFT on the even and odd indexes.                                                           |
        |_____|_____________________________________________________________________________________________________________________|
        |  4  | Calculate the omega values, which are complex numbers representing the exponential term in the Fourier transform.   |
        |_____|_____________________________________________________________________________________________________________________|
        |  5  | Combine the results of the even and odd indexes by adding and subtracting the omega values.                         |
        |_____|_____________________________________________________________________________________________________________________|


## Usage

   1. Run the program.
   2. Enter the number of rows and columns for your matrix.
   3. Perform calculations by the program.
   4. See the Fourier transform of the matrix.

## Example

   * If the input matrix is as follows:

                                                           [[ 2.0 , 3.0 , 5.0 ],
                                                    A  =    [ 1.0 , 4.0 , 6.0 ],
                                                            [ 3.0 , 2.0 , 1.0 ]]

   * In this case, our Fourier matrix will be as follows:
   
                       Fast Fourier Transform of the Matrix =  [[ 12. +0.j  ,  -3.5-0.5j          ,  -3.5-1.5j       ],
                                                                [ -10.+0.j  ,  -0.5-1.73205081j   ,  0.5+0.8660254j  ],
                                                                [  4.+0.j   ,  -0.5+0.5j          ,  -0.5+0.5j       ]]  

## References

   * [Fourier Transform](https://byjus.com/maths/fourier-transform/#:~:text=Fourier%20Transform%20is%20a%20mathematical,%2C%20RADAR%2C%20and%20so%20on)
   * [Math Documentation](https://docs.python.org/3/library/math.html)
   * [1. Fast Fourier transform](https://ww2.mathworks.cn/help/matlab/ref/fft.html?requestedDomain=cn)
   * [2. Fast Fourier transform](https://rosettacode.org/wiki/Fast_Fourier_transform#Python)
   * [Continuous Time Fourier Transform](https://staff.fnwi.uva.nl/r.vandenboomgaard/SignalProcessing/FrequencyDomain/CTNP.html)
   * [Operators used in Fourier transform](https://en.wikipedia.org/wiki/Root_of_unity)
   * [How to implement Fourier Series in Python](https://www.educative.io/answers/how-to-implement-fourier-series-in-python)