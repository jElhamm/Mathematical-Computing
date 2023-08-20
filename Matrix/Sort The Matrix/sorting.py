# This program can take a matrix as input and return it sorted.

# Mathematically we have:
                  
#           if input == [[ 20 , 15 , 10 ],                   output = [[ 0  , 5  , 10 ],
#                        [ 0  , 5  , 25 ],       ===>                  [ 15 , 20 , 25 ],   
#                        [ 30 , 35 , 40 ]]                             [ 30 , 35 , 40 ]]

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

