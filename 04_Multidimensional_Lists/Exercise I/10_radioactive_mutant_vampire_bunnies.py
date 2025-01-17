def spread_bunnies(mat, bunnies_set):
    new_bunnies = set() # second set ensures there are no duplicate bunnies
    directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]

    for b_row, b_col in bunnies_set:
        for d_row, d_col in directions:
            new_row, new_col = b_row + d_row, b_col + d_col
            # Check if position is valid (within the matrix boundaries)
            if 0 <= new_row < len(mat) and 0 <= new_col < len(mat[0]): # len(mat)
                mat[new_row][new_col] = mat[b_row][b_col]
                new_bunnies.add((new_row, new_col))

    return mat, bunnies_set.union(new_bunnies)


rows, cols = [int(x) for x in input().split()]

matrix = []
p_row, p_col = 0, 0
bunnies = set()

has_won = False
has_lost = False

for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):
        if matrix[row][col] == 'P':
            p_row, p_col = row, col
        elif matrix[row][col] == 'B':
            bunnies.add((row, col))

commands = list(input())

moves = {
    'U': lambda r, c: (r - 1, c),
    'D': lambda r, c: (r + 1, c),
    'L': lambda r, c: (r, c - 1),
    'R': lambda r, c: (r, c + 1)
}

for command in commands:
    new_p_row, new_p_col = moves[command](p_row, p_col)
    matrix, bunnies = spread_bunnies(matrix, bunnies)

    if (p_row, p_col) not in bunnies:
        matrix[p_row][p_col] = '.'

    # if player is out of bounds, player wins
    if new_p_row < 0 or new_p_row >= rows or new_p_col < 0 or new_p_col >= cols:
        has_won = True
        break

    # If player lands on a bunny after move, player loses
    p_row, p_col = new_p_row, new_p_col
    if matrix[p_row][p_col] == 'B':
        has_lost = True
        break

# Print final state of matrix
for row in matrix:
    print(''.join(row))

# Print result
if has_won:
    print(f"won: {p_row} {p_col}")
elif has_lost:
    print(f"dead: {p_row} {p_col}")

