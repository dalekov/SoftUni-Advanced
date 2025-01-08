n = int(input())

max_len = 0
longest_intersection = ''
for i in range(n):
    first_range, second_range = input().split('-')

    first_start, first_end = first_range.split(',')
    second_start, second_end = second_range.split(',')

    first_set = set(i for i in range(int(first_start), int(first_end) + 1))
    second_set = set(i for i in range(int(second_start), int(second_end) + 1))

    intersection_length = len(first_set.intersection(second_set))
    if intersection_length > max_len:
        max_len = intersection_length
        longest_intersection = first_set.intersection(second_set)

print(f"Longest intersection is {list(longest_intersection)} with length {max_len}")