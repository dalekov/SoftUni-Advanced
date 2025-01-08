from collections import deque

queue = deque()

water_available = int(input())

while True:
    name = input()

    if name == 'Start':
        break
    else:
        queue.append(name)

while True:
    command = input()

    if command == 'End':
        print(f"{water_available} liters left")
        break

    if 'refill' in command:
        water_refill = int(command.split()[1])
        water_available += water_refill
    else:
        water_consumed = int(command)
        person = queue.popleft()
        if water_available >= water_consumed:
            water_available -= water_consumed
            print(f"{person} got water")
        else:
            print(f"{person} must wait")

