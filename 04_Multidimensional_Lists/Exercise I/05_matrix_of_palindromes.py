rows, cols = map(int, input().split())

matrix = []
for i in range(1, rows + 1):
    matrix.append([])
    for j in range(cols):
        element = chr(96 + i) + chr(96 + i + j) + chr(96 + i)
        matrix[i - 1].append(element)

for i in range(rows):
    print(' '.join(matrix[i]))