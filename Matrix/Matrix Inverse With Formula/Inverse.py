# This program can receive a matrix as input and calculate its inverse matrix with a formula.
# The inverse of the matrix A is equal to Inverse of matrix A if and only if:
                    
#     [A] × [Inverse of matrix A] = [Inverse of matrix A] × [A] = [I]

# This program can inverse matrix, of square matrices up to order 4.


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
        determinant = self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        if determinant == 0:
            print("( ! The matrix cannot be inverted. ! )")
            return
        else:
            inverseMatrix = [
                [self.matrix[1][1]  / determinant, -self.matrix[0][1] / determinant],
                [-self.matrix[1][0] / determinant, self.matrix[0][0] / determinant]
            ]
            return inverseMatrix


def  banner():
    print("""
                
##########################################################################################
#                                  ***   Welcome   ***                                   #   
#             You can use this program to calculate the inverse of matrices.             #
#            To calculate the (inverse) matrix, we use the following formula:            #
#                                                                                        #
#                                           -1                                           #
#            for example:            [a , b]                 [d , -b]                    #   
#           (2x2 matrices)           [c , d]   =   1/ab-dc . [-c , a]                    #
#                                                                                        #
##########################################################################################
    """)
    
def main():
    banner()
    rows = int(input("==> Enter the number of rows: "))
    columns = int(input("==> Enter the number of columns: "))
    matrix = Matrix(rows, columns)
    matrix.enterElements()
    print("**********************************************************\n  Entered Matrix:")
    matrix.display()
    inverseMatrix = matrix.inverse()
    print("**********************************************************\n  Inverse Matrix:")
    for row in inverseMatrix:
        print(row)
    print("**********************************************************\n")

if __name__ == "__main__":
    main()
