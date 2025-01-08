occurrences = {}

nums = list(map(float, input().split()))

for num in nums:
    if num not in occurrences:
        occurrences[num] = 0
    occurrences[num] += 1

for number, occurrence in occurrences.items():
    print(f"{number:.1f} - {occurrence} times")