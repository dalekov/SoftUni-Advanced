from collections import deque

cups = deque(list(map(int, input().split()))) # queue
bottles = list(map(int, input().split())) # stack

wasted_water = 0

while cups and bottles:
    current_cup = cups[0]
    current_bottle = bottles.pop()

    difference = current_cup - current_bottle
    if difference <= 0:
        cups.popleft()
        wasted_water += abs(difference)
    elif difference > 0:
        cups[0] -= current_bottle

if not cups:
    print(f"Bottles: {' '.join(map(str, bottles))}")

elif not bottles:
    print(f"Cups: {' '.join(map(str, cups))}")

print(f"Wasted litters of water: {wasted_water}")