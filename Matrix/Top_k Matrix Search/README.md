# Matrix (Top-k) Finder

   "This program is designed to search for the top elements in a matrix using the (Top-k) algorithm.
   It allows users to enter a matrix and find the top-k elements based on their values."

## Algorithm Application

   * [Data Analysis](https://en.wikipedia.org/wiki/Data_analysis)
   * [Machine Learning](https://mitsloan.mit.edu/ideas-made-to-matter/machine-learning-explained)
   * [Data Mining](https://en.wikipedia.org/wiki/Data_mining)
   * [Network Analysis](https://www.mygreatlearning.com/blog/what-is-network-analysis/#:~:text=Network%20analysis%20is%20a%20powerful,the%20system%20as%20a%20whole.)
   * [Image Processing](https://en.wikipedia.org/wiki/Digital_image_processing) 
   * [Optimization Problems](https://en.wikipedia.org/wiki/Optimization_problem)

   These are just a few examples, and the potential applications
    of this code can vary depending on the specific requirements of a field or problem.

## Algorithm Explanation

   1. The program defines a class Matrix with the following attributes:

            _____________________________________________________________________
           |                                                                     | 
           |       'rows': the number of rows in the matrix                      |
           |       'columns': the number of columns in the matrix                |
           |       'matrix': a 2D list to store the elements of the matrix       |
           |_____________________________________________________________________|

   2. The Matrix class has the following methods:

            _______________________________________________________________________________________________
           |                                                                                               |
           |       '__init__(self, rows, columns)': Initializes the attributes of the Matrix class.        |
           |_______________________________________________________________________________________________|
           |       'enterElements(self)': Prompts the user to enter the elements for each position in      |
           |                            the matrix and stores them in the matrix attribute.                |
           |_______________________________________________________________________________________________|
           |       'display(self)':  Prints the matrix in a tabular format.                                |
           |_______________________________________________________________________________________________|
           |       '__len__(self)':  Returns the number of rows in the matrix.                             | 
           |_______________________________________________________________________________________________|
           |       'top_k_elements(self, k)': Implements the Top-k algorithm by retrieving all             |
           |                                  elements in the matrix and sorting them in                   |
           |                                  descending order. It then returns the top k elements.        |
           |_______________________________________________________________________________________________|
 
   3. The program defines a helper function 'sort_list(lst)' to sort a list in descending order.
   4. The 'main()' function is called to execute the program. It displays a banner message and prompts the user to enter the number of  rows and columns for the matrix. It creates a Matrix object and calls the 'enterElements()' method to input the matrix elements. It then calls the 'display()' method to print the entered matrix. The user is prompted to enter the value of k and the program outputs the top (k) elements in the matrix.


## References

   For the implementation of the Top-k Algorithm and efficient sorting of the list,
   the following references may be helpful:

   * [Sorting Algorithms:](https://en.wikipedia.org/wiki/Sorting_algorithm)
   * [k largest(or smallest) elements in an array](https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/)