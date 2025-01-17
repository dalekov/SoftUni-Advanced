n = int(input())

matrix = [[int(x) for x in input().split(', ')] for i in range(n)]

primary_diagonal_sum = 0
primary_diagonal_elements = []
for i in range(n):
    primary_diagonal_sum += matrix[i][i]
    primary_diagonal_elements.append(str(matrix[i][i]))

print(f"Primary diagonal: {', '.join(primary_diagonal_elements)}. Sum: {primary_diagonal_sum}")


secondary_diagonal_sum = 0
secondary_diagonal_elements = []
for i in range(n):
    secondary_diagonal_sum += matrix[i][n - i - 1]
    secondary_diagonal_elements.append(str(matrix[i][n - i - 1]))

print(f"Secondary diagonal: {', '.join(secondary_diagonal_elements)}. Sum: {secondary_diagonal_sum}")




