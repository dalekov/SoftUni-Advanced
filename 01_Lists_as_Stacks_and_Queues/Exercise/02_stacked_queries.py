stack = []

n = int(input())

for i in range(n):
    command = input()

    if '1' in command:
        number = int(command.split()[1])
        stack.append(number)
    elif command == '2':
        if stack:
            stack.pop()
    elif command == '3':
        if stack:
            print(max(stack))
    elif command == '4':
        if stack:
            print(min(stack))

stack = stack[::-1]
print(', '.join(map(str, stack)))