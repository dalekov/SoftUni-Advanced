n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
bombs = [tuple(map(int, x.split(','))) for x in input().split()]  # Parse bomb positions

for bomb in bombs:
    bomb_row, bomb_col = bomb
    if matrix[bomb_row][bomb_col] > 0:
        damage = matrix[bomb_row][bomb_col]
        for i in range(bomb_row - 1, bomb_row + 2):
            for j in range(bomb_col - 1, bomb_col + 2):
                if 0 <= i < n and 0 <= j < n and matrix[i][j] > 0:
                    matrix[i][j] -= damage

alive_cells = sum(1 for row in matrix for el in row if el > 0)
sum_alive_cells = sum(el for row in matrix for el in row if el > 0)


print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_alive_cells}")
for i in range(n):
    print(' '.join(map(str, matrix[i])))