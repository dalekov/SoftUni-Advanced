def solution(n: int, pumps: list) -> int:
    start_idx = 0
    total_balance = 0
    current_balance = 0

    for i in range(n):
        petrol, distance = pumps[i]
        current_balance += petrol - distance
        total_balance += petrol - distance

        if current_balance < 0:
            start_idx = i + 1
            current_balance = 0

    if total_balance > 0:
        return start_idx
    else:
        return -1

n = int(input())
pumps = [tuple(map(int, input().split())) for i in range(n)]

print(solution(n, pumps))