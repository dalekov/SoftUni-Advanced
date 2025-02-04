from collections import deque

bee_groups = deque([int(x) for x in input().split()]) #queue
bee_eaters_groups = [int(x) for x in input().split()] #stack

while bee_groups and bee_eaters_groups:
    curr_bee_group = bee_groups[0] #first
    curr_bee_eaters = bee_eaters_groups[-1] #last

    # Bee-eaters win:
    if curr_bee_eaters * 7 > curr_bee_group:
        curr_bee_eaters -= curr_bee_group // 7
        bee_eaters_groups[-1] = curr_bee_eaters
        bee_groups.popleft()
    # Bees win:
    elif curr_bee_eaters * 7 < curr_bee_group:
        curr_bee_group -= curr_bee_eaters * 7
        bee_groups.popleft()
        bee_groups.append(curr_bee_group)
        bee_eaters_groups.pop()
    # Tie
    else:
        bee_groups.popleft()
        bee_eaters_groups.pop()

print("The final battle is over!")
if bee_groups:
    print(f"Bee groups left: {', '.join(map(str, bee_groups))}")
elif bee_eaters_groups:
    print(f"Bee-eater groups left: {', '.join(map(str, bee_eaters_groups))}")
else:
    print("But no one made it out alive!")








