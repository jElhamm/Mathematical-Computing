# You can use this program to calculate the Fourier transform of matrices.
# This program uses the *FFT (Fast Fourier Transform)* algorithm to calculate the two-dimensional Fourier transform.
# To understand the performance and implementation of the algorithm, refer to the (README) file.

# The implementation of the algorithm has been done in this program.

import math
class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = []

    def enterElements(self):
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                element = float(input(f"==> Enter the element at position ({i+1}, {j+1}): "))
                row.append(element)
            self.matrix.append(row)
    
    def display(self):
        for row in self.matrix:
            print(row)

    # Fast Fourier Transform (FFT)
    # A method to calculate the (2D Fast Fourier Transform) matrix       
    def fft(self):
        if math.log2(self.rows) % 1 != 0 or math.log2(self.columns) % 1 != 0:               # Check if number of rows and columns are powers of 2
            print("( ! Error: Number of rows and columns must be powers of 2. ! )")
            return
        
        for i in range(self.rows):                                                          # Apply FFT on each row
            self.matrix[i] = self.fft1D(self.matrix[i])
        self.matrix = [list(col) for col in zip(*self.matrix)]                              # Transpose the matrix
        
        for i in range(self.columns):                                                       # Apply FFT on each column
            self.matrix[i] = self.fft1D(self.matrix[i])
        self.matrix = [list(col) for col in zip(*self.matrix)]                              # Transpose the matrix back

    # One-dimensional Fourier transform function
    def fft1D(self, row):
        n = len(row)
        # Base case for recursion
        if n == 1:                                                                          
            return row
        
        # Splitting the row into even and odd indexes
        evenIndexes = []
        oddIndexes = []
        for i in range(n):
            if i % 2 == 0:
                evenIndexes.append(row[i])
            else:
                oddIndexes.append(row[i])
        
        # Recursive step
        even_result = self.fft1D(evenIndexes)
        odd_result = self.fft1D(oddIndexes)

        # Calculate omega values
        omega = []
        for k in range(n//2):
            omegaValue = complex(math.cos(2 * math.pi * k / n), -math.sin(2 * math.pi * k / n))
            omega.append(omegaValue)
        
        # Combine the results
        combinedResult = [0] * n
        for k in range(n//2):
            combinedResult[k] = even_result[k] + omega[k] * odd_result[k]
            combinedResult[k + n//2] = even_result[k] - omega[k] * odd_result[k]
        return combinedResult
    

# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def  banner():
    print("""
        
##########################################################################################
#                                ***   Welcome   ***                                     #
#                                                                                        #             
#       You can use this program to calculate the Fourier transform of a matrix.         #
#                                                                                        #
#          " This program uses the *FFT (Fast Fourier Transform)* Algorithm              #
#            to calculate the 2D Fast Fourier Transform. In this program,                #
#             we perform the calculatio by implementin the FFT Algorithm. "              #
#                                                                                        #
##########################################################################################
    """)

def main():
    banner()
    rows = int(input("==> Enter the number of rows: "))
    columns = int(input("==> Enter the number of columns: "))
    matrix = Matrix(rows, columns)
    matrix.enterElements()
    print("**********************************************************\n ==> Entered Matrix:")
    matrix.display()
    print("**********************************************************\n ==> Fast Fourier Transform of the matrix:")
    matrix.fft()
    matrix.display()
    print("**********************************************************\n")

if __name__ == "__main__":
    main()

# An example of how to use the program is shown.

# Note:
#      the statement(Line 64):    omegaValue = complex(math.cos(2 * math.pi * k / n), -math.sin(2 * math.pi * k / n))

#      calculates the complex number value of the omega term used in the Fourier transform. 
#      The real part of the omega term is given by math.cos(2 * math.pi * k / n) 
#      and the imaginary part is -math.sin(2 * math.pi * k / n).