n = int(input())

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

board = [[x for x in input().split()] for _ in range(n)]

start_row, start_col = 0, 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 'S':
            start_row, start_col = i, j

resources = 100
# board[start_row][start_col] = '.'
while True:
    command = input()

    new_row, new_col = directions[command](start_row, start_col)

    # Out of bounds check:
    if not (0 <= new_row < n and 0 <= new_col < n):
        print("Mission failed! The spaceship was lost in space.")
        break

    resources -= 5


    # Meteorite cell:
    if board[new_row][new_col] == 'M':
        resources -= 5

    # Space station cell:
    if board[new_row][new_col] == 'R':
        resources = min(resources + 10, 100)

    if board[new_row][new_col] == 'P':
        print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
        if board[start_row][start_col] not in ["R", "P"]:
            board[start_row][start_col] = '.'
        break

    if board[new_row][new_col] not in ["R", "P"]:
        board[new_row][new_col] = 'S'
    if board[start_row][start_col] not in ["R", "P"]:
        board[start_row][start_col] = '.'

    # Resource check:
    if resources < 5:
        print("Mission failed! The spaceship was stranded in space.")
        break

    start_row, start_col = new_row, new_col


for row in board:
    print(' '.join(row))