# This program calculates the inverse of a square matrix using the (Gauss-Jordan) elimination method
# This program can perform inverse matrix for square matrices.


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

    def inverse(self):
        # Check if the matrix is square
        if self.rows != self.columns:
            print("( ! Cannot calculate inverse as the matrix is not square. ! )")
            return
        # Create the identity matrix
        identity = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            row = [0] * self.columns
            row[i] = 1
            identity.matrix.append(row)
        
        # Apply the (Gauss-Jordan) elimination method
        for i in range(self.rows):
            pivot = self.matrix[i][i]
            if pivot == 0:
                print("( ! Cannot calculate inverse as the matrix is singular. ! )")
                return
            # Scale the row to make the pivot element 1
            for j in range(self.columns):
                self.matrix[i][j] = self.matrix[i][j] / pivot
                identity.matrix[i][j] = identity.matrix[i][j] / pivot
            # Perform elimination on other rows
            for k in range(self.rows):
                if k != i:
                    factor = self.matrix[k][i]
                    for j in range(self.columns):
                        self.matrix[k][j] = self.matrix[k][j] - self.matrix[i][j] * factor
                        identity.matrix[k][j] = identity.matrix[k][j] - identity.matrix[i][j] * factor

        return identity


def  banner():
    print("""
                
###########################################################################################################################
#                                                ***   Welcome   ***                                                      #   
#                              You can use this program to calculate the inverse of matrices.                             #
#                                                                                                                         #
#   To calculate the (inverse) matrix, we use (Gauss-Jordan) method:                                                      #
#                                                            [1  2]                                    [1 2 | 1 0]        #
#            *** for example:  (2x2 matrices)           A =  [3  4]             ==>  Identity matrix:  [3 4 | 0 1]        #
#                                                                                                                         #
#  ==> Multiply the first row by -3 and add it to the second row to make the bottom left element (0):  [1 2  | 1 0]       #
#                                                                                                      [0 -2 | -3 1]      #
#                                                                                                                         #
#  ==> Divide the second row by -2 to make the bottom left element (1):                                [1 2 | 1 0]        #
#                                                                                                      [0 1 | 3/2 -1/2]   #
#                                                                                                                         #
#  ==>  Multiply the second row by -2 and add it to the first row to make the top left element (0):    [1 0 | -2 1]       #
#                                                                                                      [0 1 | 3/2 -1/2]   #
#                                                                                                                         #
#  ==> The left side of the augmented matrix is now the inverse of matrix B:                B^(-1)  =  [-2    1]          #
#                                                                                                      [3/2  -1/2]        #
#                                                                                                                         #          
###########################################################################################################################
        """)
    
def main():
    banner()
    rows = int(input("==> Enter the number of rows: "))
    columns = int(input("==> Enter the number of columns: "))
    MyMatrix = Matrix(rows, columns)
    MyMatrix.enterElements()
    print("**********************************************************\n  Entered Matrix:")
    MyMatrix.display()
    inverseMatrix = MyMatrix.inverse()
    print("**********************************************************\n  Inverse Matrix:")
    inverseMatrix.display()
    print("**********************************************************\n")

if __name__ == "__main__":
    main()
