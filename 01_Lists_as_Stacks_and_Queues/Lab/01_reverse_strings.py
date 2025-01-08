string = list(input())


reversed_string = []

for _ in range(len(string)):
    reversed_string.append(string.pop())

print(''.join(reversed_string))

