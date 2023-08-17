# This program can receive a matrix as an input and search 
# for the top elements in the matrix with the help of the (Top-k) Algorithm.


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

    # Sort Elements
    def sort_list(lst):
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i] < lst[j]:
                    lst[i], lst[j] = lst[j], lst[i]
        return lst
    
    # Get the number of rows of the matrix
    def __len__(self):
        return len(self.matrix)
    
    # Return the larger element
    def top_k_elements(self, k):
        top_k = []
        for i in range(len(self.matrix)):                            # Considering the length of the matrix
            for j in range(len(self.matrix[i])):                     # Considering the length of each row of the matrix       
                top_k.append(self.matrix[i][j])                      # Add any element
        top_k = Matrix.sort_list(top_k)                              # Sort the list
        return top_k[:k]