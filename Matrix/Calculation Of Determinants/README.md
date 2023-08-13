# Determinant Calculator

   This program can be used to calculate the determinants of square matrices.
   For each order of the matrix, we have a general formula for calculation, 
   and the program calculates the determinant value of the matrix with the help of these methods.

## Usage

   1. Run the program.
   2. Enter the number of rows and columns for the matrix.
   3. Enter the elements of the matrix.
   4. The program will display the entered matrix. matrix.
   5. The program will calculate and display the transpose matrix.

## Supported Matrix Sizes

   The program supports the following matrix sizes for determinant calculation:

                            **  2x2 matrices  **
                            **  3x3 matrices  **
                            **  4x4 matrices  **

## Formula

   * To calculate the determinant of a (2x2) Matrix, the following formula is used:

            A = [[ a , b ],
                 [ c , d ]]            --->   Determinants A  = ad - bc

   * To calculate the determinant of a (3x3) Matrix, the following formula is used:

            A = [[ a , b , c ],
                 [ d , e , f ],        --->   Determinants A = a(ei-fh) - b(di-fg) + c(dh-eg)
                 [ g , h , i ]]

   * To calculate the determinant of a (4x4) Matrix, the following formula is used:

            A = [[ a , b , c , d ],                              | f  g  h |     | e  g  h |     | e  f  h |     | e  f  g |
                 [ e , f , g , h ],    --->   Determinants A = a.| j  k  l | - b.| i  k  l | + c.| i  j  l | - d.| i  j  k |
                 [ i , j , k , l ],                              | n  o  p |     | m  o  p |     | m  n  p |     | m  n  o |
                 [ m , n , o , p ]]                           
                                                                                                 
## Note

   The program can calculate determinants of matrices up to (order 4). Also,
   please note that the matrix must be square, which means the number of rows 
   and columns must be equal in order to calculate the determinant.
   