n = int(input())

even = set()
odd = set()

for i in range(1, n + 1):
    name = input()

    ascii_sum = sum(ord(ch) for ch in name) // i

    if ascii_sum % 2 == 0:
        even.add(ascii_sum)
    else:
        odd.add(ascii_sum)


even_sum = sum(even)
odd_sum = sum(odd)

if even_sum == odd_sum:
    union = list(map(str, even.union(odd)))
    print(', '.join(union))
elif odd_sum > even_sum:
    difference = list(map(str, odd - even))
    print(', '.join(difference))
elif even_sum > odd_sum:
    symmetric_difference = list(map(str, odd ^ even))
    print(', '.join(symmetric_difference))
