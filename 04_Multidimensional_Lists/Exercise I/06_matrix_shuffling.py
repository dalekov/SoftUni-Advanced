rows, cols = map(int, input().split())

matrix = [[x for x in input().split()] for i in range(rows)]

while True:
    command = input().split()

    if command[0] == 'END':
        break

    if len(command) == 5 and command[0] == 'swap':
        try:
            row1, col1, row2, col2 = map(int, command[1:])
            if 0 <= row1 < rows and 0 <= col1 < cols and 0 <= row2 < rows and 0 <= col2 < cols:
                matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
                for i in range(rows):
                    print(' '.join(map(str, matrix[i])))
            else:
                print("Invalid input!")
        except ValueError:
            print("Invalid input!")
    else:
        print("Invalid input!")