from collections import deque

contestants = deque([int(x) for x in input().split()])
pies = [int(x) for x in input().split()]

while contestants and pies:
    curr_contestant = contestants[0]
    curr_pie = pies[-1]

    if curr_contestant > curr_pie:
        contestants.popleft()
        contestants.append(curr_contestant - curr_pie)
        pies.pop()
    elif curr_contestant == curr_pie: # Exact match, remove both
        contestants.popleft()
        pies.pop()
    elif curr_contestant < curr_pie:
        curr_pie -= curr_contestant
        if curr_pie == 1 and len(pies) != 1:
            pies.pop()
            pies[-1] += 1
        else:
            pies[-1] = curr_pie
        contestants.popleft()


if contestants and not pies:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(map(str, contestants))}")

elif not contestants and not pies:
    print("We have a champion!")

elif not contestants and pies:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(map(str, pies))}")