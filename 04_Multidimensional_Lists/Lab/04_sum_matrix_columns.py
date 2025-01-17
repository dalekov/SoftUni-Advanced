rows, columns = map(int, input().split(', '))

# Building the matrix:
matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)


for col in range(columns):
    total = 0
    for row in range(rows):
        total += matrix[row][col]
    print(total)

