n = int(input())

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

board = [[x for x in input()] for _ in range(n)]

start_row, start_col = 0, 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 'B':
            start_row, start_col = i, j

energy = 15
collected_nectar = 0
times_restored = 0
while True:
    command = input()

    new_row, new_col = directions[command](start_row, start_col)
    energy -= 1


    # Bee leaves the field and gets moved to the opposite side of the field:
    if not (0 <= new_row < n and 0 <= new_col < n):
        board[start_row][start_col] = '-'
        # Diagonal mirroring (if moving off both row & column)
        if new_row < 0 and new_col < 0:  # Top-left -> Bottom-right
            new_row, new_col = n - 1, n - 1
        elif new_row < 0 and new_col >= n:  # Top-right -> Bottom-left
            new_row, new_col = n - 1, 0
        elif new_row >= n and new_col < 0:  # Bottom-left -> Top-right
            new_row, new_col = 0, n - 1
        elif new_row >= n and new_col >= n:  # Bottom-right -> Top-left
            new_row, new_col = 0, 0
        else:
            # Edge wrapping (horizontal/vertical)
            if new_row < 0:  # Out from the top, appear at the bottom
                new_row = n - 1
            elif new_row >= n:  # Out from the bottom, appear at the top
                new_row = 0

            if new_col < 0:  # Out from the left, appear on the right
                new_col = n - 1
            elif new_col >= n:  # Out from the right, appear on the left
                new_col = 0

        board[new_row][new_col] = 'B'

    # Number, bee collects nectar:
    if board[new_row][new_col].isdigit():
        collected_nectar += int(board[new_row][new_col])
        board[new_row][new_col] = 'B'
        board[start_row][start_col] = '-'

    # Hive is reached:
    elif board[new_row][new_col] == 'H':
        board[start_row][start_col] = '-'
        board[new_row][new_col] = 'B'
        if collected_nectar >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")
        break
    else:
        board[start_row][start_col] = '-'
        board[new_row][new_col] = 'B'


    if energy <= 0 and collected_nectar < 30:
        print("This is the end! Beesy ran out of energy.")
        break

    elif energy <= 0 and collected_nectar >= 30:
        if times_restored < 1:
            energy += collected_nectar - 30
            collected_nectar = 30
            times_restored += 1

            if energy <= 0:
                print("This is the end! Beesy ran out of energy.")
        else:
            print("This is the end! Beesy ran out of energy.")
            break



    start_row, start_col = new_row, new_col

for row in board:
    print(''.join(row))
