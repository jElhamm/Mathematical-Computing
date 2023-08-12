# Matrix Inverse Calculator 

   This program calculates the inverse of a square matrix using the Gauss-Jordan elimination method. The program can perform inverse matrix calculations for square matrices only.

## Introduction

   1. Run the program.
   2. Enter the number of rows and columns for the matrix.
   3. Enter the elements of the matrix row by row.
   4. The program will display the entered matrix.
   5. The program will calculate the inverse matrix using the Gauss-Jordan elimination method.
   6. The program will display the inverse matrix.is implemented using a specific programming language.

## Example

  The Gauss-Jordan method is a well-known algorithm for finding the inverse of a matrix.
  Here is a brief explanation of the steps involved in the Gauss-Jordan method for matrix inversion with an example description:

   For example, consider a 2x2 matrix:

                        A = [[1 , 2],
                             [3 , 4]]

   * The inverse of this matrix can be calculated as follows:

                        A = [[1 , 2 | 1 , 0],
                             [3 , 4 | 0 , 1]]
   
   * Multiply the first row by -3 and add it to the second row to make the bottom left element 0:

                        A = [[1 , 2  |  1 ,  0],
                             [0 , -2 | -3 , 1]]
    
   * Divide the second row by -2 to make the bottom left element 1:

                        A = [[1 , 2 | 1 , 0],
                             [0 , 1 | 3/2 , -1/2]]

   * Multiply the second row by -2 and add it to the first row to make the top left element 0:

                        A = [[1 , 0 | -2 , 1],
                             [0 , 1 | 3/2 , -1/2]]

   * The left side of the augmented matrix is the inverse of matrix A. Therefore, the inverse of matrix A is:

                        A^(-1) = [[-2  ,  1],
                                  [3/2 , -1/2]]

## Note

   The operations applied to the matrix are displayed in each step for reference.
   The matrix must be square (i.e., the number of rows and columns must be the same) since only square matrices have inverses.
   The inverse of a matrix is not possible if the matrix is singular (i.e., it does not have full rank).