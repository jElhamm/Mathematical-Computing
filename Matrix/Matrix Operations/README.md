## Matrix Calculator

This program is a matrix calculator that allows users to perform basic operations on matrices, including addition, subtraction, and multiplication.

# Features

  * Addition of Matrices: The program can add multiple matrices together. 
    All matrices being added must have the same number of rows and columns. 
    The resulting matrix will be the sum of the corresponding elements in each input matrix.
     

  * Subtraction of Matrices: The program can subtract one matrix from another. 
     All matrices being subtracted must have the same number of rows and columns. 
     The resulting matrix will be the difference of the corresponding elements in each input matrix.

  * Multiplication of Matrices: The program can multiply multiple matrices together. 
    The number of columns in the first matrix must be equal to the number of rows in the second matrix.
    The resulting matrix will have dimensions equal to the number of rows in the first matrix and the number of columns in the second matrix. Each element in the resulting matrix is calculated by taking the dot product of the corresponding row in the first matrix and the corresponding column in the second matrix.

## Usage

   1. Run the program.
   2. Enter the number of rows and columns for the matrix.
   3. Enter the elements of the matrix.
   4. The program will display the entered matrix.
   5. The program will perform the selected operation on the matrices and display the resulting matrix. 

## Formula

   * The sum of the matrices is calculated as follows:

                        A = [[ a , b ],
                             [ c , d ]]  
                                                 --->   A + B =  [[ a + e  ,  b + f ],
                        B = [[ e , f ],                           [ c + g  ,  d + h ]]
                             [ g , h ]]

   * Subtraction of matrices is calculated as follows: 
       
                        A = [[ a , b ],
                             [ c , d ]]  
                                                 --->   A - B =  [[ a - e  ,  b - f ],
                        B = [[ e , f ],                           [ c - g  ,  d - h ]]
                             [ g , h ]]
                             
   * Matrix multiplication is calculated as follows:       
                        
                        A = [[ a , b , c ],    
                             [ d , e , f ]] 
                                                 --->   A X B =  [[ ag + bi + ck  ,  ah + bg + cl ],                    
                        B = [[ g , h ]                            [ dg + ei + fk  ,  dh + eg + fl ]]
                             [ i , g ]
                             [ k , l ]]

## Note

   In addition and subtraction, all matrices must have the same number of rows and columns.
   Also, in the multiplication section, the number of columns of the first matrix must be equal to 
   the number of rows of the second matrix. As a result, the resulting matrix will have dimensions equal to
   the number of rows of the first matrix and the number of columns of the second matrix.
