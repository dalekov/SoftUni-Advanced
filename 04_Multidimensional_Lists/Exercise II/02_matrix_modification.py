n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]


while True:
    command = input().split()
    if command[0] == 'END':
        break

    x = int(command[1])
    y = int(command[2])
    value = int(command[3])

    if 0 <= x < len(matrix) and 0 <= y < len(matrix):
        if command[0] == 'Add':
            matrix[x][y] += value
        elif command[0] == 'Subtract':
            matrix[x][y] -= value
    else:
        print("Invalid coordinates")

for i in range(len(matrix)):
    print(' '.join([str(x) for x in matrix[i]]))