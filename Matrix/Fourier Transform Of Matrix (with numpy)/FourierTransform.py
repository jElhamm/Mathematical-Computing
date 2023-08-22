# You can use this program to calculate the Fourier transform of matrices.
# We use the (numpy) library to perform calculations.
# This program uses the *FFT (Fast Fourier Transform)* Algorithm to calculate the 2D Fast Fourier Transform


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
    


# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def  banner():
    print("""
        
###########################################################################################################
#                                   ***   Welcome   ***                                                   #
#                                                                                                         #             
#             You can use this program to calculate the Fourier transform of a matrix.                    #
#          This program uses the *FFT (Fast Fourier Transform)* Algorithm to calculate the                #
#       2D Fast Fourier Transform. To perform the Fourier transform of the input matrix, you can          #
#    use the numpy library. This library has fft function to perform fast Fourier transform of matrix.    #
#                                                                                                         #
###########################################################################################################
    """)

def main():
    banner()
    rows = int(input("==> Enter the number of rows: "))
    columns = int(input("==> Enter the number of columns: "))
    matrix = Matrix(rows, columns)
    matrix.enterElements()
    print("**********************************************************\n ==> Entered Matrix:")
    matrix.display()
    
    fft_matrix = matrix.fft()
    print("**********************************************************\n ==> Fast Fourier Transform of the matrix:")
    print(fft_matrix)
    print("**********************************************************\n")

if __name__ == "__main__":
    main()

# An example of how to use the program is shown.