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

    # Sort Function
    def sort(self):
        for i in range(self.rows):                                   # Repeat in each row
            for j in range(self.columns):                                # Repeat in each column
                for k in range(self.rows):                                   # Comparing the current element with each element in the matrix
                    for l in range(self.columns):   
                        if self.matrix[i][j] < self.matrix[k][l]:                # If the current element is smaller than the compared element,
                            self.matrix[i][j], self.matrix[k][l] = self.matrix[k][l], self.matrix[i][j]        #  the elements are swapped.


# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def  banner():
    print("""
        
######################################################################################################
#                                     ***   Welcome   ***                                            #
#                                                                                                    #             
#                   You can use this program to sort the elements in a matrix.                       #
#                                        for example:                                                #
#                            (You can sort matrices in any order.)                                   #
#                                                                                                    #
#               if input == [[ 20 , 15 , 10 ],            output = [[ 0  , 5  , 10 ],                #
#                            [ 0  , 5  , 25 ],    ===>              [ 15 , 20 , 25 ],                #
#                            [ 30 , 35 , 40 ]]                      [ 30 , 35 , 40 ]]                #
#                                                                                                    #
######################################################################################################
    """)

def main():
    banner()
    rows = int(input("==> Enter the number of rows: "))
    columns = int(input("==> Enter the number of columns: "))
    matrix = Matrix(rows, columns)
    matrix.enterElements()
    print("**********************************************************\n==> Original Matrix:")
    matrix.display()
    matrix.sort()
    print("**********************************************************\n==> Sorted Matrix:")
    matrix.display()
    print("**********************************************************\n")

if __name__ == "__main__":
    main()