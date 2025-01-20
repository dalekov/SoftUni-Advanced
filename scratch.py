rows, cols = [int(x) for x in input().split()]

matrix = []
p_row, p_col = 0, 0
bunnies = set()

has_won = False
has_lost = False


for row in range(rows):
    matrix.append(input())