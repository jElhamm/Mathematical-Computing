# This program can perform basic operations on matrices. 
# (There is no limit on the number of input matrices)

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
    
    def add(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                row = []
                for j in range(self.columns):
                    element = self.matrix[i][j] + other.matrix[i][j]
                    row.append(element)
                result.matrix.append(row)
            return result
        else:
            print("( ! Cannot add the matrices. They have different dimensions. ! )       ")
    
    def subtract(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                row = []
                for j in range(self.columns):
                    element = self.matrix[i][j] - other.matrix[i][j]
                    row.append(element)
                result.matrix.append(row)
            return result
        else:
            print("( ! Cannot subtract the matrices. They have different dimensions. ! )       ")
    
    def multiply(self, other):
        if self.columns == other.rows:
            result = Matrix(self.rows, other.columns)
            for i in range(self.rows):
                row = []
                for j in range(other.columns):
                    element = 0
                    for k in range(self.columns):
                        element += self.matrix[i][k] * other.matrix[k][j]
                    row.append(element)
                result.matrix.append(row)
            return result
        else:
            print("( ! Cannot multiply the matrices. ! )")
            print("( The number of columns in the first matrix must be equal to the number of rows in the second matrix. )")

def  banner():
    print("""
        
##########################################################################################
#                              ***   Welcome   ***                                       #   
#        You can use this program to perform mathematical operations on matrices.        #
#                The operations you can perform include the following:                   #
#                                                                                        #   
#                      1. Addition of matrices                (+)                        #
#                      2. Subtraction of matrices             (-)                        #
#                      3. Multiplication of matrices          (*)                        #
#                                                                                        #     
##########################################################################################
        """)
    
def main():
    banner()
    UserInput = int(input("==> Please enter the number of the operation you want to perform: "))
    numMatrices = int(input("==> Enter the number of matrices: "))

    # Create matrices
    matrices = []
    for i in range(numMatrices):
        rows = int(input(f"==> Enter the number of rows for matrix {i+1}: "))
        columns = int(input(f"==> Enter the number of columns for matrix {i+1}: "))
        matrix = Matrix(rows, columns)
        matrix.enterElements()
        matrices.append(matrix)

    # Display matrices
    for i, matrix in enumerate(matrices):
        print("\n******************************************")
        print(f"  Matrix {i+1}:")
        matrix.display()

    # Addition of matrices 
    if UserInput == 1:
        # Checking if all matrices have the same rows and columns
        equalDimensions = all(matrix.rows == matrices[0].rows and matrix.columns == matrices[0].columns for matrix in matrices)
        if not equalDimensions:
            print("( ! Error: All matrices must have the same number of rows and columns. ! )       ")
            return
        addition = matrices[0]
        for i in range(1, numMatrices):
            addition = addition.add(matrices[i])
        print("\n******************************************\n  ==> Result of addition:")
        addition.display()
        print("******************************************\n")

    # Subtraction of matrices
    elif UserInput == 2:
        # Checking if all matrices have the same rows and columns
        equalDimensions = all(matrix.rows == matrices[0].rows and matrix.columns == matrices[0].columns for matrix in matrices)
        if not equalDimensions:
            print("( ! Error: All matrices must have the same number of rows and columns. ! )       ")
            return
        subtraction = matrices[0]
        for i in range(1, numMatrices):
            subtraction = subtraction.subtract(matrices[i])
        print("\n******************************************\n  ==> Result of subtraction:")
        subtraction.display()
        print("******************************************\n")

    # multiplication of matrices
    elif UserInput == 3:
        multiplication = matrices[0]
        for i in range(1, numMatrices):
            multiplication = multiplication.multiply(matrices[i])
        print("\n******************************************\n  ==> Result of multiplication:")
        if multiplication is not None:
            multiplication.display()
            print("******************************************\n")

if __name__ == '__main__':
    main()