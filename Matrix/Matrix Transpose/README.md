# Matrix Transpose 

  This program can be used to calculate the transfer matrix.

          ****  The mathematical form of how to calculate the transfer matrix is ​​as follows:  ****

                           [A] = m.n   ===>    Matrix transpose [A] = n.m

         (The component a(i,j) in matrix B is equal to the component a(j,i) in Matrix transpose [A].)

## Usage

   1. Run the program.
   2. Enter the number of rows and columns for the matrix.
   3. Enter the elements of the matrix row by row.
   4. Once you have entered all the elements, the program will display the entered 
      matrix.
   5. The program will then calculate the inverse of the matrix.
   6. Finally, the program will display the inverse matrix.


## Example

  To find the transpose of the matrix, we follow these steps:

   1. Create a new matrix with the number of rows equal to the number of columns in the original matrix, and the number of 
      columns equal to the number of rows in the original matrix. This new matrix will be the transpose matrix.

   2. Iterate through each element in the original matrix and place it in the corresponding position in the transpose matrix. 
      The position of the element in the original matrix is (i,j), and its corresponding position in the transpose matrix is 
      (j,i).

   3. Once all elements have been placed in the transpose matrix, print the transpose matrix.



  Here's a step-by-step example using the matrix : 

                     [[1 , 2 , 3],
                      [4 , 5 , 6]]

   * Create a new matrix with 3 rows and 2 columns:

                     [[0 , 0],
                      [0 , 0],
                      [0 , 0]]
 
  * Place the elements of the original matrix in the transpose matrix:

         Element 1 (position 1 , 1) --> Transpose position (1 , 1)
         Element 2 (position 1 , 2) --> Transpose position (2 , 1)
         Element 3 (position 1 , 3) --> Transpose position (3 , 1)
         Element 4 (position 2 , 1) --> Transpose position (1 , 2)
         Element 5 (position 2 , 2) --> Transpose position (2 , 2)
         Element 6 (position 2 , 3) --> Transpose position (3 , 2)

  * The transpose matrix is:

                  [[1 , 4],
                   [2 , 5],
                   [3 , 6]]

## Note

   The program only works for square matrices. If the number of rows and columns are not equal, it will not calculate the transpose matrix.