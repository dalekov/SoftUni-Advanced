n = int(input())

board = [[x for x in input()] for _ in range(n)]

possible_moves = [
    (-2, -1), (-2, 1), (-1, -2), (-1, 2),
    (1, -2), (1, 2), (2, -1), (2, 1)
]

def count_attacks(x, y):
    attacks = 0
    for dx, dy in possible_moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 'K':
            attacks += 1

    return attacks


removed_knights = 0
while True:
    max_attacks = 0
    knight_to_remove = None

    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                attacks = count_attacks(i, j)
                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_to_remove = i, j

    if max_attacks == 0:
        break

    i, j = knight_to_remove
    board[i][j] = '0'
    removed_knights += 1

print(removed_knights)