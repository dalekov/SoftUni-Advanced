rows, cols = map(int, input().split(', '))

# Building the matrix
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

max_sum = float('-inf')
largest_submatrix = []
for i in range(rows - 1):
    for j in range(cols - 1):
        current_sum = matrix[i][j] + matrix[i + 1][j] + matrix[i][j + 1] + matrix[i + 1][j + 1]
        if current_sum > max_sum:
            max_sum = current_sum
            largest_submatrix = [[matrix[i][j], matrix[i][j + 1]], [matrix[i + 1][j], matrix[i + 1][j + 1]]]


print(' '.join(map(str, largest_submatrix[0])))
print(' '.join(map(str, largest_submatrix[1])))
print(max_sum)