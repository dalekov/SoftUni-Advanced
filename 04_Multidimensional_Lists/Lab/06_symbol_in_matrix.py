n = int(input())

matrix = []
for _ in range(n):
    matrix.append(input())

symbol = input()
is_found = False

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            is_found = True
            break
    if is_found:
        break

if not is_found:
    print(f"{symbol} does not occur in the matrix")