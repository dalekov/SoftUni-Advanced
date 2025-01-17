rows, cols = map(int, input().split())

matrix = [[int(x) for x in input().split()] for i in range(rows)]

max_sum = float('-inf')
largest_submatrix = []
for i in range(rows - 2):
    for j in range(cols - 2):
        current_sum = (matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] +
                       matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2] +
                       matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2])

        if current_sum > max_sum:
            max_sum = current_sum
            largest_submatrix = [
    [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
    [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
    [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]
]

print(f"Sum = {max_sum}")
for i in range(3):
    print(' '.join(map(str, largest_submatrix[i])))