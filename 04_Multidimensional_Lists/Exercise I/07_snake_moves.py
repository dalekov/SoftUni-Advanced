rows, cols = map(int, input().split())
snake = input()

matrix = [['' for _ in range(cols)] for _ in range(rows)]

index = 0
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = snake[index % len(snake)]
        index += 1

    if i % 2 == 1:
        matrix[i].reverse()

for k in range(rows):
    print(''.join(matrix[k]))