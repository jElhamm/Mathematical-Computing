# This program can receive a matrix as input and calculate its transpose matrix.
# The mathematical form of how to calculate the transfer matrix:

#        [B] = m.n   ===>    Matrix transpose [B] = n.m
# The component bij in matrix B is equal to the component bji in Matrix transpose [B].


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

    def transpose(self):
        result = Matrix(self.columns, self.rows)
        for i in range(self.columns):
            row = []
            for j in range(self.rows):
                element = self.matrix[j][i]
                row.append(element)
            result.matrix.append(row)
        return result

def  banner():
    print("""
                
##########################################################################################
#                                  ***   Welcome   ***                                   #   
#             You can use this program to calculate the transpose of matrices.           #
#        To find (Transpose) a matrix, the position of rows and columns is changed.      #
#                                                                                        #
#                                                T      [a , d]                           #
#               for example:          [a , b , c]       [b , e]                           #   
#                                     [d , e , f]   =   [c , f]                           #
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
    transpose_matrix = matrix.transpose()
    print("**********************************************************\n  Transposed Matrix:")
    transpose_matrix.display()
    print("**********************************************************\n")

if __name__ == "__main__":
    main()
