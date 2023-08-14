% To show the Transpose matrix, the following function can be used.
% It should be noted that to use this function you have to give a matrix as input so that it can perform the operation for you.
% At the end of the program, how to use the function is explained.

% The mathematical form of how to calculate the transfer matrix:

%               [B] = m.n   ===>    Matrix transpose [B] = n.m
% The component bij in matrix B is equal to the component bji in Matrix transpose [B].


function result = calculateTranspose(matrix)
    % initial value and determining the number of rows and columns of the matrix
    [rows, columns] = size(matrix);
    result = zeros(columns, rows);
    
    for i = 1:rows
        for j = 1:columns
            % Moving elements
            result(j, i) = matrix(i, j);
        end   
    end
end
    



% For the program to work, you need to add this section to your code:
% Example of using this function

% You must enter your matrix as follows:
matrix = [1 2 3; 4 5 6; 7 8 9];

% Now we call the function to execute:
calculateTranspose(matrix)