directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

presents = int(input())

n = int(input()) # Size of matrix

board = [[x for x in input().split()] for _ in range(n)]

nice_kids = sum(row.count('V') for row in board)
nice_kids_given = 0

current_row, current_col = 0, 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 'S':
            current_row, current_col = i, j

while True:
    command = input()

    # If command is received, end program.
    if command == 'Christmas morning':
        break

    # Move Santa:
    next_row, next_col = directions[command](current_row, current_col)

    # Ensure the next move is within bounds:
    if 0 <= next_row < n and 0 <= next_col < n:
        if board[next_row][next_col] == 'V': # Nice kid cell
            presents -= 1
            nice_kids -= 1
            nice_kids_given += 1

        elif board[next_row][next_col] == 'C':  # Cookie cell
            # Distribute presents to surrounding cells
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
                adj_row, adj_col = next_row + dr, next_col + dc
                if 0 <= adj_row < n and 0 <= adj_col < n:
                    if board[adj_row][adj_col] in 'XV' and presents > 0:
                        if board[adj_row][adj_col] == 'V':
                            nice_kids -= 1
                            nice_kids_given += 1
                        presents -= 1
                        board[adj_row][adj_col] = '-'

        board[current_row][current_col] = '-'
        board[next_row][next_col] = 'S'
        current_row, current_col = next_row, next_col

    # If Santa runs out of presents and no , end program.
    if nice_kids and presents <= 0:
        print(f"Santa ran out of presents!")
        break


for row in board:
    print(' '.join(row))

if nice_kids == 0:
    print(f"Good job, Santa! {nice_kids_given} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")

