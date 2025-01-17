rows, cols = map(int, input().split(', '))

matrix = []
total = 0

for i in range(rows):
    row = [int(x) for x in input().split(', ')]
    total += sum(row)
    matrix.append(row)

print(total)
print(matrix)

