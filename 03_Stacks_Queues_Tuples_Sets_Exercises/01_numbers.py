first = set(map(int, input().split()))
second = set(map(int, input().split()))

n = int(input())

for i in range(n):
    command = input().split()

    new_command = command[0] + ' ' + command[1]
    if 'Add First' == new_command:
        nums = command[2:]
        first.update(list(map(int, nums)))

    if 'Add Second' == new_command:
        nums = command[2:]
        second.update(list(map(int, nums)))

    if 'Remove First' == new_command:
        nums = command[2:]
        for num in nums:
            first.discard(int(num))

    if 'Remove Second' == new_command:
        nums = command[2:]
        for num in nums:
            second.discard(int(num))

    if 'Check Subset' == new_command:
        print("True" if first >= second or first <= second else "False")

first = list(sorted(first))
second = list(sorted(second))

print(', '.join(map(str, first)))
print(', '.join(map(str, second)))

