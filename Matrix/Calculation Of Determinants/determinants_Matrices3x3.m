% The following function can be used to calculate the determinant of Matrices (3x3).
% It should be noted that to use this function you have to give a matrix as input so that it can perform the operation for it.
% At the end of the program, how to use the function is explained.

% For (3x3) matrices, the opposite formula is used:

%                       if [[ a , b , c ],
#                           [ d , e , f ],        ===>  Determinant = a(ei-fh) - b(di-fg) + c(dh-eg)
#                           [ g , h , i ]]
% 



% Implementation of the formula:
% determinant = (a11 * (a22 * a33 - a23 * a32)) - (a12 * (a21 * a33 - a23 * a31)) + (a13 * (a21 * a32 - a22 * a31))

function determinant = calculateDeterminant(matrix)
    % The initial value for the result
    [rows, columns] = size(matrix);
    
    % Examining the structure of the matrix
    if rows == 3 && columns == 3
        determinant = (
              (matrix(1, 1) * (matrix(2, 2) * matrix(3, 3) - matrix(2, 3) * matrix(3, 2))) 
            - (matrix(1, 2) * (matrix(2, 1) * matrix(3, 3) - matrix(2, 3) * matrix(3, 1))) 
            + (matrix(1, 3) * (matrix(2, 1) * matrix(3, 2) - matrix(2, 2) * matrix(3, 1)))
            );
    else
        disp('( ! Cannot calculate the determinant. The matrix is not 3x3. ! )');
    end
end



% For the program to work, you need to add this section to your code:
% Example of using this function

% You must enter your matrix as follows:
matrix = [11 2 3; 24 5 6; 7 18 9];

% Now we call the function to execute:
determinant = calculateDeterminant(matrix)