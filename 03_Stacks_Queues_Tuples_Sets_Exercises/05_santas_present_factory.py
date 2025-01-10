from collections import deque

magic_levels_required = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400
}

crafted_presents = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0
}

task_done = False

materials = [int(x) for x in input().split()] # stack
magic_levels = deque([int(x) for x in input().split()]) # queue

while materials and magic_levels:
    current_materials = materials[-1]
    current_magic_level = magic_levels[0]

    multiplication = current_materials * current_magic_level

    for key, value in magic_levels_required.items():
        if multiplication == value:
            crafted_presents[key] += 1
            materials.pop()
            magic_levels.popleft()
            break
    else:
        if multiplication < 0:
            summ = current_materials + current_magic_level
            materials.pop()
            magic_levels.popleft()
            materials.append(summ)
        elif multiplication > 0:
            magic_levels.popleft()
            materials[-1] += 15
        elif current_magic_level == 0 and current_materials == 0:
            magic_levels.popleft()
            materials.pop()
        elif current_materials == 0:
            materials.pop()
        elif current_magic_level == 0:
            magic_levels.popleft()

if crafted_presents["Doll"] > 0 and crafted_presents["Wooden train"] > 0:
    task_done = True
elif crafted_presents["Teddy bear"] > 0 and crafted_presents["Bicycle"] > 0:
    task_done = True

if task_done:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")


for present in sorted(crafted_presents.keys()):
    if crafted_presents[present] > 0:
        print(f"{present}: {crafted_presents[present]}")