% To show the Inverse matrix, the following function can be used.
% In this program, the formula method is used to calculate the Inverse matrix.
% It should be noted that to use this function you have to give a matrix as input so that it can perform the operation for you.
% At the end of the program, how to use the function is explained.

% The inverse of the matrix A is equal to Inverse of matrix A if and only if:

%    [A] × [Inverse of matrix A] = [Inverse of matrix A] × [A] = [I]


function result = calculateInverse(matrix)
    [rows, columns] = size(matrix);
    
    % Check if matrix is square
    if rows == columns
        det_matrix = det(matrix);

        if det_matrix ~= 0
            % Calculate inverse matrix
            adjoint_matrix = calculateAdjoint(matrix);
            result = (1/det_matrix) * adjoint_matrix;

        else
            % Matrix is not invertible
            fprintf('Matrix is not invertible.\n');
            result = [];
        end

    else
    % Matrix is not square
        fprintf('Matrix is not square.\n');
        result = [];
    end
end

% Calculate Adjoint Matrix
function result = calculateAdjoint(matrix)
    [rows, columns] = size(matrix);
    result = zeros(rows, columns);

    % Loop through each element of the matrix
    for i = 1:rows
        for j = 1:columns
            % Calculate the cofactor by taking the determinant of the submatrix
            cofactor = (-1)^(i+j) * det(matrix([1:i-1, i+1:end],[1:j-1, j+1:end]));
            result(i,j) = cofactor;
        end
    end
    
    result = result;
end
    



% For the program to work, you need to add this section to your code:
% Example of using this function

% You must enter your matrix as follows:
matrix = [11 2 37; 24 5 6; 87 8 9];

% Now we call the function to execute:
inverse_matrix = calculateInverse(matrix);
disp(inverse_matrix);