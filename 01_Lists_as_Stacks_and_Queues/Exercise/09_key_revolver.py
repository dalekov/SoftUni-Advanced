from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split())) # stack
locks = deque(list(map(int, input().split()))) # queue
intelligence_value = int(input()) # starting balance

bullets_used = 0
while locks and bullets:
    bullets_used += 1

    # Bang
    if locks[0] >= bullets.pop():
        print("Bang!")
        locks.popleft()
    # Ping
    else:
        print("Ping!")

    intelligence_value -= bullet_price

    if bullets_used == gun_barrel_size and bullets:
        print("Reloading!")
        bullets_used = 0

    if not locks:
        print(f"{len(bullets)} bullets left. Earned ${intelligence_value}")
        break

    if not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break
