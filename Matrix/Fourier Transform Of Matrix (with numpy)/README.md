# Fourier transform of Matrix

   The [Fourier Transform](https://en.wikipedia.org/wiki/Fourier_transform) is a mathematical technique that transforms a signal from its time domain representation to its frequency domain representation.
   It decomposes a signal into its constituent frequencies, allowing us to analyze and manipulate the different frequency components of the signal.

   The Fourier transform can be applied to various types of signals, including [*continuous-time signals*](https://en.wikipedia.org/wiki/Discrete_time_and_continuous_time), [*discrete-time signals*](https://en.wikipedia.org/wiki/Discrete_time_and_continuous_time), and *two-dimensional signals* like images. In this program, we focus on the 2D Fourier transform, specifically for matrices.


## [Fast Fourier Transform (FFT)](https://en.wikipedia.org/wiki/Fast_Fourier_transform)

        *****************************************************************************************************************
        *                                                                                                               *
        *            The Fast *Fourier Transform (FFT)* is an efficient algorithm used to compute the                   *
        *        discrete Fourier transform (DFT) of a sequence or an array. It reduces the computational               *
        *    complexity of the DFT from   [ O(n^2) to O(n log n) ]   , making it  much *faster for large data sets.     *
        *                                                                                                               *
        *****************************************************************************************************************

## 2D Fast Fourier Transform

        *****************************************************************************************************************
        *                                                                                                               *
        *                         The *2D Fast Fourier Transform (2D FFT)* extends the concept                          *
        *                  of the FFT to two-dimensional arrays or matrices. It can be used to analyze                  *
        *              the spatial frequencies present in an image or perfor various signal processing tasks.           *
        *                                                                                                               *
        *****************************************************************************************************************

## Usage

   1. Run the program.
   2. Enter the number of rows and columns for your matrix.
   3. Perform calculations by the program.
   4. See the Fourier transform of the matrix.

## Example

   * If the input matrix is ​​as follows:

                                                   [[ 2.0 , 3.0 , 5.0 ],
                                            A  =    [ 1.0 , 4.0 , 6.0 ],
                                                    [ 3.0 , 2.0 , 1.0 ]]

   * In this case, our Fourier matrix will be as follows:
   
            Fast Fourier Transform of the Matrix =  [[ 12. +0.j  ,  -3.5-0.5j          ,  -3.5-1.5j       ],
                                                     [ -10.+0.j  ,  -0.5-1.73205081j   ,  0.5+0.8660254j  ],
                                                     [  4.+0.j   ,  -0.5+0.5j          ,  -0.5+0.5j       ]]


## References

   * [Fourier Transform](https://byjus.com/maths/fourier-transform/#:~:text=Fourier%20Transform%20is%20a%20mathematical,%2C%20RADAR%2C%20and%20so%20on)
   * [NumPy Documentation](https://numpy.org/doc/)
   * [Discrete Fourier Transform (numpy.fft)](https://numpy.org/doc/stable/reference/routines.fft.html)
   * [Real Python - An Introductory Guide to FFT](https://realpython.com/python-scipy-fft/)
   * [Continuous Time Fourier Transform](https://staff.fnwi.uva.nl/r.vandenboomgaard/SignalProcessing/FrequencyDomain/CTNP.html)
   * [Applying Fourier Transform In Python Using Numpy.fft](https://pythontic.com/visualization/signals/fouriertransform_fft)
