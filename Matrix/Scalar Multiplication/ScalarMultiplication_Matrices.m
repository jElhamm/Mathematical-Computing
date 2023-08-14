% The following function can be used for matrix Scalar multiplication.
% It should be noted that to use this function, you must give a matrix and a number as input so that it can perform the operation for you.
% At the end of the program, how to use the function is explained.

% The mathematical form of how to calculate the multiplication of a number in a matrix:

%         Scalar = s         m = [[ a , b ],      ===>      s.m = [[ sa , sb ],
%                                 [ c , d ]]                       [ sc , sd ]]


function result = multiplyScalar(matrix, scalar)
    % initial value and determining the number of rows and columns of the matrix
    [rows, columns] = size(matrix);
    result = zeros(rows, columns);

    for i = 1:rows
        for j = 1:columns
            % do multiplication
            result(i, j) = matrix(i, j) * scalar;
        end
    end
end



% For the program to work, you need to add this section to your code:
% Example of using this function

% You have to enter your matrix and the number you want to multiply by as follows:
matrix = [1 2 3; 4 5 6]
scalar = 2

% Now we call the function to execute:
multiplyScalar(matrix, scalar)