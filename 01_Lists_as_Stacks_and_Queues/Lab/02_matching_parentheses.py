text = input()

parentheses = []

for i in range(len(text)):
    if text[i] == '(' :
        parentheses.append(i)
    elif text[i] == ')':
        start_idx = parentheses.pop()
        print(text[start_idx: i + 1])