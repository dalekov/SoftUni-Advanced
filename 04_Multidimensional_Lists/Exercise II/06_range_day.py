directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

board = [[x for x in input().split()] for _ in range(5)]

sum_targets = sum(row.count('x') for row in board)
completed_targets = []

start_row, start_col = 0, 0
for i in range(5):
    for j in range(5):
        if board[i][j] == 'A':
            start_row, start_col = i, j

n = int(input())

no_targets_left = False
for _ in range(n):
    command = input().split()

    action = command[0]
    direction = command[1]

    if action == 'shoot':
        current_row, current_col = start_row, start_col
        while True:
            next_row, next_col = directions[direction](current_row, current_col)
            if not (0 <= next_row < 5 and 0 <= next_col < 5):
                break
            if board[next_row][next_col] == 'x':
                completed_targets.append([next_row, next_col])
                board[next_row][next_col] = '.'

                # Check to see if any targets left
                if sum(row.count('x') for row in board) == 0:
                    no_targets_left = True


                break
            current_row, current_col = next_row, next_col

    elif action == 'move':
        steps = int(command[2])
        for _ in range(steps):
            new_row, new_col = directions[direction](start_row, start_col)
            if (0 <= new_row < 5 and 0 <= new_col < 5) and (board[new_row][new_col] == '.'):
                board[start_row][start_col] = '.'
                board[new_row][new_col] = 'A'
                start_row, start_col = new_row, new_col

    if no_targets_left:
        break

if no_targets_left:
    print(f"Training completed! All {sum_targets} targets hit.")
else:
    print(f"Training not completed! {sum_targets - len(completed_targets)} targets left.")

for target in completed_targets:
    print(target)