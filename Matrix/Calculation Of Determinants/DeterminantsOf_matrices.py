# In this program, I can calculate square matrices up to order 4.

# For (2x2) matrices, the opposite formula is used:   if [a , b]
#                                                        [c , d]            ===>  Determinant = ad - bc
# 
# For (3x3) matrices, the opposite formula is used:   if [a , b , c]
#                                                        [d , e , f]        ===>  Determinant = a(ei-fh) - b(di-fg) + c(dh-eg)
#                                                        [g , h , i]
# 
# For (4x4) matrices, the opposite formula is used:   if [a , b , c , d]                          |f  g  h|     |e  g  h|
#                                                        [e , f , g , h]    ===>  Determinant = a.|j  k  l| - b.|i  k  l| 
#                                                        [i , j , k , l]                          |n  o  p|     |m  o  p|
#                                                        [m , n , o , p]                           
#                                                                                                 |e  f  h|     |e  f  g|
#                                                                                             + c.|i  j  l| - d.|i  j  k|
#                                                                                                 |m  n  p|     |m  n  o| 


class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.elements = [[0 for _ in range(columns)] for _ in range(rows)]

    def enterElements(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.elements[i][j] = int(input(f"==> Enter element at position ({i+1},{j+1}): "))

    def __getitem__(self, indices):
        row, col = indices
        return self.elements[row][col]
        
    def display(self):
        for row in self.elements:
            print(row)

    # Determinant of the matrix 2x2
    def calculateDeterminant2x2(self):
        if self.rows != self.columns:
            print("( ! Determinant can only be calculated for square matrices. ! )")
            return None
        
        determinant = self[0,0]*self[1,1] - self[0,1]*self[1,0]
        return determinant
    
    # Determinant of the matrix 3x3
    def calculateDeterminant3x3(self):
        if self.rows != self.columns:
            print("( ! Determinant can only be calculated for square matrices. ! )")
            return None
        
        determinant = (
              self[0,0]*(self[1,1]*self[2,2] - self[1,2]*self[2,1])
            - self[0,1]*(self[1,0]*self[2,2] - self[1,2]*self[2,0])
            + self[0,2]*(self[1,0]*self[2,1] - self[1,1]*self[2,0])
        )
        return determinant
    
    # Determinant of the matrix 4x4
    def calculateDeterminant4x4(self):
        if self.rows != self.columns:
            print("( ! Determinant can only be calculated for square matrices. ! )")
            return None
        
        determinant = (
              self[0,0]*(self[1,1]*(self[2,2]* self[3,3] - self[2,3]*self[3,2])
            - self[1,2]*(self[2,1]*self[3,3] - self[2,3]*self[3,1])
            + self[1,3]*(self[2,1]*self[3,2] - self[2,2]*self[3,1])) -
            
              self[0,1]*(self[1,0]*(self[2,2]* self[3,3] - self[2,3]*self[3,2])
            - self[1,2]*(self[2,0]*self[3,3] - self[2,3]*self[3,0])
            + self[1,3]*(self[2,0]*self[3,2] - self[2,2]*self[3,0])) +
            
              self[0,2]*(self[1,0]*(self[2,1]* self[3,3] - self[2,3]*self[3,1])
            - self[1,1]*(self[2,0]*self[3,3] - self[2,3]*self[3,0])
            + self[1,3]*(self[2,0]*self[3,1] - self[2,1]*self[3,0])) -
                
              self[0][3]*(self[1][0]*(self[2][1]* self[3][2] - self[2][2]*self[3][1])
            - self[1][1]*(self[2][0]*self[3][2] - self[2][2]*self[3][0])
            + self[1][2]*(self[2][0]*self[3][1] - self[2][1]*self[3][0]))
        )
        return determinant

def  banner():
    print("""
        
##########################################################################################
#                                  ***   Welcome   ***                                   #   
#             You can use this program to calculate determinants of matrices.            #
#                                                                                        #
#        Matrices that you can calculate their determinants:        |  2x2 matrices  |   #
#                                                                   |  3x3 matrices  |   #   
#        [! Note that to calculate the determinant,                 |  4x4 matrices  |   #
#            the matrix must be square, that is,                                         #
#              the number of rows and columns must be equal. !]                          #
##########################################################################################
        """)
    
def main():
    rows = int(input("==> Enter the number of rows in the matrix: "))
    columns = int(input("==> Enter the number of columns in the matrix: "))
    matrix = Matrix(rows, columns)
    matrix.enterElements()
    print("Entered Matrix:")
    matrix.display()
    print("##########################################################################################")
    
    if rows == 2 and columns == 2:
        determinant = matrix.calculateDeterminant2x2()
    elif rows == 3 and columns == 3:
        determinant = matrix.calculateDeterminant3x3()
    elif rows == 4 and columns == 4:
        determinant = matrix.calculateDeterminant4x4()
    else:
        print("( ! Determinant can only be calculated for 2x2, 3x3, or 4x4 matrices. ! )")
        return
    print("==> The determinant is: ", determinant)

if __name__ == "__main__":
    main()
    