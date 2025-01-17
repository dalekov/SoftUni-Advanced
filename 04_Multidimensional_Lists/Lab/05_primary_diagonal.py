n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

total = 0
for j in range(n):
    total += matrix[j][j]

print(total)