n = int(input())

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

board = [list(input()) for _ in range(n)]

enemy_aircrafts = []
start_row, start_col = 0, 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 'J':
            start_row, start_col = i, j
        elif board[i][j] == 'E':
            enemy_aircrafts.append((i, j))

armor = 300
while True:
    command = input()

    new_row, new_col = directions[command](start_row, start_col)

    # Enemy aircraft:
    if board[new_row][new_col] == 'E':
        enemy_aircrafts.remove((new_row, new_col))
        armor -= 100
        board[start_row][start_col] = '-'

        if armor <= 0:
            print(f"Mission failed, your jetfighter was shot down! Last coordinates [{new_row}, {new_col}]!")
            board[new_row][new_col] = 'J'
            break
        elif not enemy_aircrafts:
            print("Mission accomplished, you neutralized the aerial threat!")
            board[new_row][new_col] = 'J'
            break

    # Repair station:
    elif board[new_row][new_col] == 'R':
        armor = 300
        board[start_row][start_col] = '-'
        board[new_row][new_col] = '-'

    board[start_row][start_col] = '-'
    board[new_row][new_col] = 'J'
    start_row, start_col = new_row, new_col

for row in board:
    print(''.join(row))