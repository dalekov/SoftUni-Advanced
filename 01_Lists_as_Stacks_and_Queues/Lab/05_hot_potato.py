from collections import deque

queue = deque(list(input().split()))
n = int(input())


count = 1
while len(queue) != 1:
    if count % n == 0:
        print(f"Removed {queue.popleft()}")
    else:
        qx
    count += 1

print(f"Last is {queue[0]}")

