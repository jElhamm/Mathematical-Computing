# You can use this program to calculate the Laplace transform of numerical matrices.
  
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

    # Apply the Laplace transform to each element in the matrix
    def laplaceTransform(self):
        s = float(input("==> Enter the value of s: "))                    # Get the value of s from the user
        result = [[0] * self.columns for _ in range(self.rows)]           # Create an empty matrix for the result
        # result = np.zeros((self.rows, self.columns))
        
        for i in range(self.rows):                                        #  Apply the Laplace transform
            for j in range(self.columns):
                result[i][j] = self.matrix[i][j] / (s + 1)
        return result
    
# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def  banner():
    print("""
        
################################################################################################
#                                   ***   Welcome   ***                                        #
#                                                                                              #             
#     You can use this program to calculate the Laplace transform of a (numerical Matrix).     #
#       Consider f(t) as a function of the independent variable t. The Laplace transform       #
#           (f(t)) is equal to a function of a new variable s, which can generally be          #
#                        complex. The variable (s) must be numeric.                            #
#                                                                                              #
#                            for example:      value of s == 3                                 #
#                                                                                              #
#            A == [[ 2.0 , 4.0 ],    ===>    Transformed Matrix == [[ 0.4  , 0.8 ],            #
#                  [ 6.0 , 8.0 ]]                                   [ 1.2 , 1.6 ]]             #
#                                                                                              #
################################################################################################
    """)

def main():
    banner()
    rows = int(input("==> Enter the number of rows: "))
    columns = int(input("==> Enter the number of columns: "))
    matrix = Matrix(rows, columns)
    matrix.enterElements()
    print("**********************************************************\n ==> Entered Matrix:")
    matrix.display()
    
    transformed_matrix = matrix.laplaceTransform()
    print("**********************************************************\n ==> Transformed Matrix:")
    for row in transformed_matrix:
        print(row)
    print("**********************************************************\n")

if __name__ == "__main__":
    main()

# An example of how to use the program is shown.