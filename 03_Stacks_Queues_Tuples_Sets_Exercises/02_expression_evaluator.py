sequence = list(input().split())

for ch in sequence[:]:
    idx = sequence.index(ch)
    if ch == '+':
        total = sum(int(num) for num in sequence[:idx])
        sequence[:idx + 1] = [total]
    elif ch == '-':
        total = int(sequence[0])
        for num in sequence[1:idx]:
            total -= int(num)
        sequence[:idx + 1] = [total]

    elif ch == '*':
        total = int(sequence[0])
        for num in sequence[1:idx]:
            total *= int(num)
        sequence[:idx + 1] = [total]

    elif ch == '/':
        total = int(sequence[0])
        for num in sequence[1:idx]:
            total //= int(num)
        sequence[:idx + 1] = [total]

print(sequence[0])
