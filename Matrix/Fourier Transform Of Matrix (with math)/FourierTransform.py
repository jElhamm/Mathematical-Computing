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