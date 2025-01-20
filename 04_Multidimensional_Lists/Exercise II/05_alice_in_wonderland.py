n = int(input())

board = [[x for x in input().split()] for _ in range(n)]

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

start_row, start_col = 0, 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 'A':
            start_row, start_col = i, j

board[start_row][start_col] = '*'
game_over = False
tea_collected = 0
while tea_collected < 10 and not game_over:
    command = input()

    new_row, new_col = directions[command](start_row, start_col)

    if not (0 <= new_row < n and 0 <= new_col < n):
        game_over = True

    if board[new_row][new_col] == 'R':
        board[new_row][new_col] = '*'
        game_over = True

    if board[new_row][new_col].isdigit():
        tea_collected += int(board[new_row][new_col])

    board[start_row][start_col] = '*'
    board[new_row][new_col] = '*'
    start_row, start_col = new_row, new_col

if game_over:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for row in board:
    print(' '.join(row))