n = int(input())

matrix = [[int(x) for x in input().split(' ')] for i in range(n)]

primary_diagonal_sum = 0
for i in range(n):
    primary_diagonal_sum += matrix[i][i]

secondary_diagonal_sum = 0
for i in range(n):
    secondary_diagonal_sum += matrix[i][n - i - 1]

diff = abs(primary_diagonal_sum - secondary_diagonal_sum)
print(diff)




