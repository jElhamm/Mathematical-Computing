% The following function can be used to calculate the determinant of matrices 2.2.
% It should be noted that to use this function you have to give a matrix as input so that it can perform the operation for it.
% At the end of the program, how to use the function is explained.

% For (2x2) matrices, the opposite formula is used:
%           A = [[ a , b ],
%                [ c , d ]]            --->   Determinants A  = ad - bc


function determinant = calculateDeterminant(matrix)
    [rows, columns] = size(matrix);
    
    if rows == 3 && columns == 3
        determinant = (matrix(1, 1) * matrix(2, 2)) - (matrix(1, 2) * matrix(2, 1));
    else
        disp('( ! Cannot calculate the determinant. The matrix is not 2x2. ! )');
    end
end



% For the program to work, you need to add this section to your code:
% Example of using this function

% You must enter your matrix as follows:
matrix = [1 2; 3 4]

% Now we call the function to execute:
determinant = calculateDeterminant(matrix)
