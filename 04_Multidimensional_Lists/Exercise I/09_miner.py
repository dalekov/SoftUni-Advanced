n = int(input())
commands = input().split()

matrix = [[x for x in input().split()] for _ in range(n)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

total_coal = sum(row.count('c') for row in matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 's':
            miner_curr_pos = (i, j)
            break

for command in commands:
    new_row = miner_curr_pos[0] + directions[command][0]
    new_col = miner_curr_pos[1] + directions[command][1]
    
    if 0 <= new_row < n and 0 <= new_col < n:
        miner_curr_pos = (new_row, new_col)
        if matrix[new_row][new_col] == 'c':
            total_coal -= 1
            matrix[new_row][new_col] = '*'
            if total_coal == 0:
                print(f"You collected all coal! ({new_row}, {new_col})")
                break
        elif matrix[new_row][new_col] == 'e':
            print(f"Game over! ({new_row}, {new_col})")
            break

else:
    print(f"{total_coal} pieces of coal left. ({new_row}, {new_col})")