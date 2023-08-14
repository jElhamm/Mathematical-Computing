# This program can receive a matrix and a number as input and calculate the matrix containing the multiplication of these two.
# The mathematical form of how to calculate the multiplication of a number in a matrix:

#                            [ a , b ]                 [ sa , sb ]
#        Scalar = s     m =  [ c , d ]     ===>  s.m = [ sc , sd ]
 

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

    def multiplyByNumber(self, number):
        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i][j] *= number

def  banner():
    print("""
        
#########################################################################################################
#                                       ***   Welcome   ***                                             #   
#       You can use this program to calculate the multiplication of a scalar Number in a Matrix.        # 
#              To do this, it is enough to multiply that Number in each row of the Matrix               #
#                           And form a new Matrix with the results.                                     #
#                                                                                                       #
#                                         [ 4 , 0 ]      [ 8 , 0 ]                                      #   
#                 for example:        2 . [ 1 , -9 ]  =  [ 2 , -18 ]                                    #
#                                                                                                       #
#                       (A number that is multiplied by a Matrix is called a "Scalar".)                 #
#                                                                                                       #
#########################################################################################################
    """)

def main():
    banner()
    rows = int(input("==> Enter the number of rows: "))
    columns = int(input("==> Enter the number of columns: "))
    matrix = Matrix(rows, columns)
    matrix.enterElements()
    print("**********************************************************\n  Entered Matrix:")
    matrix.display()
    number = float(input("\n ==> Enter a number to multiply the matrix: "))
    matrix.multiplyByNumber(number)
    matrix.display()
    print("**********************************************************\n")


if __name__ == "__main__":
    main()