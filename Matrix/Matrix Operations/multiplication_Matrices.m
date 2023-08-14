% The following function can be used to multiply matrices.
% It should be noted that in order to use this function, you must give two matrices as input so that it can perform the operation for you.
% At the end of the program, how to use the function is explained.

% Matrix multiplication is calculated face to face:

%                         if [[ a , b , c ],     [[ g , h ],     [[ ag+bi+ck , ah+bg+cl ],
%                             [ d , e , f ]]  X   [ i , g ],  =   [ dg+ei+fk , dh+eg+fl ]]
%                                                 [ k , l ]]


function result = multiplyMatrices(matrix1, matrix2)
    % Determining the number of rows and columns of the matrix
    [rows1, columns1] = size(matrix1);
    [rows2, columns2] = size(matrix2);
    
    % Checking the equality of dimensions of two matrices
    if columns1 == rows2
        % The initial value for the result
        result = zeros(rows1, columns2);

        for i = 1:rows1
            for j = 1:columns2
                for k = 1:columns1
                    % Calculation of multiplication
                    result(i, j) = result(i, j) + matrix1(i, k) * matrix2(k, j);
                end
            end
        end

    else
        disp('( ! Cannot multiply the matrices. The number of columns in the first matrix must be equal to the number of rows in the second matrix. !)');
    end
end



% For the program to work, you need to add this section to your code:
% Example of using this function

% You must enter your matrix as follows:
matrix1 = [1 2 3; 4 5 6];
matrix2 = [7 8; 9 10; 11 12];

% Now we call the function to execute:
multiplyMatrices(matrix1, matrix2)