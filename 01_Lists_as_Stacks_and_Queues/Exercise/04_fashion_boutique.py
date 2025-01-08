clothes = list(map(int, input().split()))
capacity = int(input())
racks = 0

total = 0
for i in range(len(clothes) - 1, -1, -1):
    next_ =  clothes[i]
    total += next_
    if total == capacity or total + clothes[i - 1] > capacity or i == 0:
        racks += 1
        total = 0

print(racks)



