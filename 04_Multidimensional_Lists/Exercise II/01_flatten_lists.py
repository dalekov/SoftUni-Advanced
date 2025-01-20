lists = input().split('|')

result = []
for sublist in reversed(lists):
    numbers = sublist.split()
    result.extend(numbers)

print(' '.join(result))

