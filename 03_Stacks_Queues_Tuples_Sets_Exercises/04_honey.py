from collections import deque

working_bees = deque([int(x) for x in input().split()]) # queue - take first
nectar = [int(x) for x in input().split()] # stack - take last
operators = deque(input().split())

total_honey = 0
while working_bees and nectar:
    current_bee = working_bees[0]
    current_nectar = nectar[-1]

    if current_bee > current_nectar:
        nectar.pop() # we remove current nectar
        continue
    elif current_nectar >= current_bee: # nectar is collected.
        operator = operators.popleft()

        if operator == '+':
            honey_made = current_bee + current_nectar
        elif operator == '-':
            honey_made = current_bee - current_nectar
        elif operator == '*':
            honey_made = current_bee * current_nectar
        elif operator == '/' and current_nectar != 0:
            honey_made = current_bee / current_nectar
        else:
            honey_made = 0

        total_honey += abs(honey_made)

        nectar.pop()
        working_bees.popleft()

print(f"Total honey made: {total_honey}")

if working_bees:
    print(f"Bees left: {', '.join(map(str, working_bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")