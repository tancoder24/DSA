def rotate_matrix(matrix):
    matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3], matrix[1][3], matrix[2][3], matrix[3][3], matrix[3][2], matrix[3][1], matrix[3][0], matrix[2][0], matrix[1][0] = matrix[0][1], matrix[0][2], matrix[0][3], matrix[1][3], matrix[2][3], matrix[3][3], matrix[3][2], matrix[3][1], matrix[3][0], matrix[2][0], matrix[1][0], matrix[0][0]
    matrix[1][1], matrix[1][2], matrix[2][2], matrix[2][1] = matrix[2][1], matrix[1][1], matrix[1][2], matrix[2][2] 
    return matrix

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

for rows in matrix:
    for data in rows:
        print( data ^ 4 )  