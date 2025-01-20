n = int(input())

# Setting up the board
board = [[x for x in input().split()] for _ in range(n)]

# Map with directions
directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

b_row, b_col = 0, 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 'B':
            b_row, b_col = i, j

best_direction = ''
max_eggs = float('-inf')
best_path = ''
for direction in directions:
    path = []
    current_eggs = 0
    new_row, new_col = b_row, b_col
    while True:
        new_row, new_col = directions[direction](new_row, new_col)

        if not (0 <= new_row < n and 0 <= new_col < n):
            break

        if board[new_row][new_col] == 'X':
            break

        current_eggs += int(board[new_row][new_col])
        path.append([new_row, new_col])
    if current_eggs >= max_eggs:
        max_eggs = current_eggs
        best_direction = direction
        best_path = path

print(best_direction)
print(*[f"[{pos[0]}, {pos[1]}]" for pos in best_path], sep='\n')
print(max_eggs)
