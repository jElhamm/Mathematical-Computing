# You can use this program to calculate the Fourier transform of matrices.
# We use the (numpy) library to perform calculations.

# Fourier series method is used in this program.


import numpy as np
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

    # Two-dimensional Fourier transform function 
    def fft(self):                                                  
        matrix_np = np.array(self.matrix)               # Convert the matrix to numpy array                        
        fft_matrix = np.fft.fft2(matrix_np)             # Compute the Fast Fourier Transform of the matrix
        return fft_matrix                               # output == The final result of the two-dimensional fast Fourier transform
    

