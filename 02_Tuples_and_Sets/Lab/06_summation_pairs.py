numbers = list(map(int, input().split()))
target = int(input())

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == '':
            continue

        if numbers[j] == '':
            continue

        if numbers[i] + numbers[j] == target:
            print(f"{numbers[i]} + {numbers[j]} = {target}")

            numbers[i] = ''
            numbers[j] = ''