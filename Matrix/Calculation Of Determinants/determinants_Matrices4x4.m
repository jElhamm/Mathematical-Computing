% The following function can be used to calculate the determinant of matrices (4x4).
% It should be noted that to use this function you have to give a matrix as input so that it can perform the operation for it.
% At the end of the program, how to use the function is explained.

% For (4x4) matrices, the opposite formula is used:

%                        if [[ a , b , c , d ],                          | f  g  h |     | e  g  h|
%                            [ e , f , g , h ],    ===>  Determinant = a.| j  k  l | - b.| i  k  l| 
%                            [ i , j , k , l ],                          | n  o  p |     | m  o  p|
%                            [ m , n , o , p ]]                           
%                                                                        | e  f  h |     | e  f  g |
%                                                                    + c.| i  j  l | - d.| i  j  k |
%                                                                        | m  n  p |     | m  n  o | 



% Implementation of the formula:
% determinant = a* ( f*(kp-lo) - g*(jp-ln) + h*(jo-kn) ) - b* ( e*(kp-lo) - g*(ip-lm) + h*(io-km) ) 
%             + c* ( e*(jp-ln) - f*(ip-lm) + h*(in-jm) ) - d* ( e*(jo-kn) - f*(io-km) + g*(in-jm) )

function determinant = calculateDeterminant(matrix)
    % The initial value for the result
    [rows, columns] = size(matrix);

    % Examining the structure of the matrix
    if (rows == columns && rows == 4)

    % Implementation of the formula: 
        determinant =(
          matrix(1,1)* (matrix(2,2) *(matrix(3,3)* matrix(4,4)- matrix(4,3) *matrix(3,4)) 
        - matrix(2,3)* (matrix(3,2) *matrix(4,4) - matrix(4,2)* matrix(3,4)) 
        + matrix(2,4)* (matrix(3,2) *matrix(4,3) - matrix(4,2)* matrix(3,3))) 
        - matrix(1,2)* (matrix(2,1) *(matrix(3,3)* matrix(4,4)- matrix(4,3) *matrix(3,4))
        - matrix(2,3)* (matrix(3,1) *matrix(4,4) - matrix(4,1)* matrix(3,4)) 
        + matrix(2,4)* (matrix(3,1) *matrix(4,3) - matrix(4,1)* matrix(3,3))) 
        + matrix(1,3)* (matrix(2,1) *(matrix(3,2)* matrix(4,4)- matrix(4,2) *matrix(3,4)) 
        - matrix(2,2)* (matrix(3,1) *matrix(4,4) - matrix(4,1)* matrix(3,4)) 
        + matrix(2,4)* (matrix(3,1) *matrix(4,2) - matrix(4,1)* matrix(3,2))) 
        - matrix(1,4)* (matrix(2,1) *(matrix(3,2)* matrix(4,3)- matrix(4,2) *matrix(3,3)) 
        - matrix(2,2)* (matrix(3,1) *matrix(4,3) - matrix(4,1)* matrix(3,3)) 
        + matrix(2,3)* (matrix(3,1) *matrix(4,2) - matrix(4,1)* matrix(3,2)))
        );
        
    else
        disp('( ! The matrix does not have the correct dimensions. ! )');
    end
end



% For the program to work, you need to add this section to your code:
% Example of using this function

% You must enter your matrix as follows:
matrix = [1 12 53 44; 53 66 87 8; 9 100 11 2; 13 14 15 6];

% Now we call the function to execute:
determinant = calculateDeterminant(matrix)