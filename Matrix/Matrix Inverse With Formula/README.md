# Matrix Inverse Calculator 

   There are different ways to calculate the inverse of a matrix.
   This program, which has the ability to calculate the inverse matrix, uses the method finding the inverse of the matrix with 
   normalized method (Adjuvant method).
   
   The inverse of a matrix A is represented by A^-1 and it satisfies the following condition:           

                           A × A^-1 = A^-1 × A = I

                       (Where I is the identity matrix.)

## Introduction

   1. Run the program.
   2. Enter the number of rows and columns for the matrix.
   3. Enter the elements of the matrix row by row.
   4. Once you have entered all the elements, the program will display the entered matrix.
   5. The program will then calculate the inverse of the matrix.
   6. Finally, the program will display the inverse matrix.

## Formula
   To calculate the inverse of a 2x2 matrix, the following formula is used:

                            A^-1 = 1 / (ad - bc) * |d  -b|
                                                   |-c  a|

                    (Where a, b, c, and d are the elements of the matrix A.)

## Example

  
  Here is a brief explanation of the steps involved in the method for matrix inversion with an example description:

   For example, consider a 2x2 matrix:

                            A = [[3 , 2],
                                 [4 , 1]]

   * To calculate the inverse of this matrix, we use the formula:

                            ( inverseMatrix = 1/determinant * adjointMatrix )
   
   * Step 1: Find the determinant

                            ( determinant = (3 * 4) - (2 * 1) = 10 )
    
   * Step 2: Find the adjoint matrix

                            adjointMatrix = [[ 4 , -2],
                                             [-1 ,  3]]

   * Step 3: Calculate the inverse matrix

                            inverseMatrix = 1/10 * adjointMatrix = [[4/10  , -2/10],
                                                                    [-1/10 , 3/10]]

   * Simplifying the fractions, we get:

                            inverseMatrix = [[2/5 , -1/5],
                                             [-1/10 , 3/10]]

  * The inverse matrix of the given matrix is:

                            A^-1 = [2/5 , -1/5]
                                   [-1/10 , 3/10]

## Note

   The program can only calculate the inverse of square matrices up to order 4. If the determinant of the matrix is 0,
   it means that the matrix cannot be inverted.