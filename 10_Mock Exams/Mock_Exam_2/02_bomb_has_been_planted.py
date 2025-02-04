rows, cols = map(int, input().split(", "))

board = [list(input()) for _ in range(rows)]
seconds = 16

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

ct_row, ct_col = 0, 0
for i in range(rows):
    for j in range(cols):
        if board[i][j] == 'C':
            ct_row, ct_col = i, j

killed = False
not_found_bomb = True
while seconds > 0:
    command = input()

    if command == 'defuse':
        if board[ct_row][ct_col] != 'B':
            seconds -= 2

        if board[ct_row][ct_col] == 'B':
            not_found_bomb = False

            if seconds >= 4:
                seconds -= 4
                board[ct_row][ct_col] = 'D'
                print("Counter-terrorist wins!")
                print(f"Bomb has been defused: {seconds} second/s remaining.")
            else:
                board[ct_row][ct_col] = 'X'
                print("Terrorists win!")
                print("Bomb was not defused successfully!")
                print(f"Time needed: {4 - seconds} second/s.")
            break

    else:
        seconds -= 1
        new_row, new_col = directions[command](ct_row, ct_col)

        if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
            continue
        if board[new_row][new_col] == 'T':
            killed = True
            board[new_row][new_col] = '*'
            print("Terrorists win!")
            break

        ct_row, ct_col = new_row, new_col

if not_found_bomb and not killed:
    print(f"Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: {abs(seconds)} second/s.")

for row in board:
    print(''.join(row))