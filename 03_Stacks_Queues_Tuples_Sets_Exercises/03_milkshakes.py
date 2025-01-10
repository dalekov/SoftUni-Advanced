from collections import deque

chocolates = list(map(int, input().split(', '))) # stack
milks = deque(list(map(int, input().split(', ')))) # queue
milkshakes = 0

while milkshakes < 5 and (chocolates and milks):
    while chocolates and chocolates[-1] <= 0:
        chocolates.pop()

    while milks and milks[0] <= 0:
        milks.popleft()

    if not chocolates or not milks:
        break

    chocolate = chocolates[-1] # last chocolate
    milk = milks[0] # first milk

    if chocolate == milk:
        milkshakes += 1
        chocolates.pop()
        milks.popleft()
    else:
        milks.append(milks.popleft())
        chocolates[-1] -= 5


if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(map(str, chocolates)) if chocolates else 'empty'}")
print(f"Milk: {', '.join(map(str, milks)) if milks else 'empty'}")