from collections import deque

food = int(input())

orders = deque(list(map(int, input().split())))
print(max(orders))

while True:
    food_consumed = orders[0]
    if food - food_consumed < 0:
        print(f"Orders left: {' '.join(map(str, orders))}")
        break
    else:
        orders.popleft()
        food -= food_consumed

    if not orders:
        print("Orders complete")
        break

