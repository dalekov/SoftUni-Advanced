line = input()
stack = []

matching_brackets = {')': '(', ']': '[', '}': '{'}
for ch in line:
    if ch in '([{':
        stack.append(ch)
    elif ch in ')]}':
        if stack and stack[-1] == matching_brackets[ch]:
            stack.pop()
        else:
            print("NO")
            break
else:
    if not stack:
        print("YES")
