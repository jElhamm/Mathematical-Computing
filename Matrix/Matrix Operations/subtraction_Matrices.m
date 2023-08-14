% The following function can be used to subtract matrices.
% It should be noted that in order to use this function, you must give two matrices as input so that it can perform the operation for you.
% At the end of the program, how to use the function is explained.

% Subtraction of matrices is calculated face to face: 

%                  if [[ a , b ],     [[ e , f ],    [[ a-e , b-f ],
%                      [ c , d ]]  -   [ g , h ]]  =  [ c-g , d-h ]]


function result = subtractMatrices(matrix1, matrix2)
    % Determining the number of rows and columns of the matrix 
    [rows1, columns1] = size(matrix1);
    [rows2, columns2] = size(matrix2);
    
    % Checking the equality of dimensions of two matrices
    if (rows1 == rows2) && (columns1 == columns2)
        % The initial value for the result
        result = zeros(rows1, columns1);

        for i = 1:rows1
            for j = 1:columns1
                % do subtraction
                result(i, j) = matrix1(i, j) - matrix2(i, j);
            end
        end

    else
        disp('( ! Cannot subtract the matrices. They have different dimensions. ! )');
    end
end



% For the program to work, you need to add this section to your code:
% Example of using this function

% You must enter your matrix as follows:
matrix1 = [1 2 3; 4 5 6]
matrix2 = [7 8 9; 10 11 12]

% Now we call the function to execute:
subtractMatrices(matrix1, matrix2)