n = int(input())

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

board = [list(input()) for _ in range(n)]

start_row, start_col = 0, 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 'P':
            start_row, start_col = i, j

health = 100
while True:
    command = input()

    new_row, new_col = directions[command](start_row, start_col)

    if not (0 <= new_row < n and 0 <= new_col < n):
        continue

    # Monster cell
    if board[new_row][new_col] == 'M':
        health -= 40
        if health > 0: # player survives
            board[new_row][new_col] = '-'
        else: # player dies, game ends.
            health = 0
            board[new_row][new_col] = 'P'
            print("Player is dead. Maze over!")
            break

    # Health potion cell
    elif board[new_row][new_col] == 'H':
        health = min(health + 15, 100)
        board[new_row][new_col] = '-'

    # X - Exit
    elif board[new_row][new_col] == 'X':
        board[start_row][start_col] = '-'
        board[new_row][new_col] = 'P'
        print("Player escaped the maze. Danger passed!")
        break

    board[start_row][start_col] = '-'
    start_row, start_col = new_row, new_col

print(f"Player's health: {health} units")
for row in board:
    print(''.join(row))