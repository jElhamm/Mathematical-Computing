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