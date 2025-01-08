chars = {}

line = input()

for ch in line:
    if ch not in chars:
        chars[ch] = 0
    chars[ch] += 1

sorted_line = sorted(chars.keys(), key=lambda x: x)


for ch in sorted_line:
    print(f"{ch}: {chars[ch]} time/s")