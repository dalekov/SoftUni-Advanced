n = int(input())

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

board = [[x for x in input().split()] for _ in range(n)]

start_row, start_col = 0,0
for i in range(n):
    for j in range(n):
        if board[i][j] == 'P':
            start_row, start_col = i, j

stars = 2
board[start_row][start_col] = '.'
while True:
    command = input()

    next_row, next_col = directions[command](start_row, start_col)

    # Out of bounds, player gets punished and teleported back to start -> 0,0
    if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
        next_row, next_col = 0, 0

    # Player collect 10 stars and wins
    if stars >= 10:
        print("You won! You have collected 10 stars.")
        break

    # Player loses all stars and loses:
    if stars <= 0:
        print("Game over! You are out of any stars.")
        break

    # Star cell:
    if board[next_row][next_col] == '*':
        stars += 1
        board[next_row][next_col] = '.'

    # Obstacle cell
    elif board[next_row][next_col] == '#':
        stars -= 1
        if stars <= 0:
            print("Game over! You are out of any stars.")
            break
        continue # We continue, player does not move

    start_row, start_col = next_row, next_col

print(f"Your final position is [{start_row}, {start_col}]")
board[start_row][start_col] = 'P'
for row in board:
    print(' '.join(row))


