with open("numbers.txt") as file:
    total = 0
    for line in file:
        total += int(line)

    print(total)