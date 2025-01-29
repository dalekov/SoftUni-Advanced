class MatrixSizeError(Exception):
    pass

class MatrixContentError(Exception):
    pass

def rotate_matrix(matrix):
    matrix_length = len(matrix)

    # Check if matrix is square
    if not all(len(row) == matrix_length for row in matrix):
        raise MatrixSizeError("The size of the matrix is not a perfect square")

    # Check if the matrix contains only integers
    for row in matrix:
        for ch in row:
            if not ch.isdigit():
                raise MatrixContentError("The matrix must consist of only integers")

    for i in range(matrix_length):
        for j in range(i + 1, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()

    return matrix


mtrx = []

while True:
    line = input().split()

    if not line:
        break
    mtrx.append(line)


rotate_matrix(mtrx)
for row in mtrx:
    print(*row, sep=' ')