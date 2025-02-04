from collections import deque

strengths = [int(x) for x in input().split()] # stack
accuracies = deque([int(x) for x in input().split()])

goals = 0
while strengths and accuracies:
    curr_strength = strengths[-1]
    curr_accuracy = accuracies[0]

    curr_sum = curr_strength + curr_accuracy
    if curr_sum == 100:
        goals += 1
        strengths.pop()
        accuracies.popleft()

    elif curr_sum < 100:
        if curr_strength < curr_accuracy:
            strengths.pop()
        elif curr_strength > curr_accuracy:
            accuracies.popleft()
        elif curr_strength == curr_accuracy:
            accuracies.popleft()
            strengths[-1] = curr_strength + curr_accuracy

    elif curr_sum > 100:
        strengths[-1] -= 10
        accuracies.append(accuracies.popleft())


if goals == 3:
    print("Paul scored a hat-trick!")
elif goals == 0:
    print("Paul failed to score a single goal.")
elif goals > 3:
    print("Paul performed remarkably well!")
elif 0 < goals < 3:
    print("Paul failed to make a hat-trick.")

if goals:
    print(f"Goals scored: {goals}")

if strengths:
    print(f"Strength values left: {', '.join(map(str, strengths))}")
if accuracies:
    print(f"Accuracy values left: {', '.join(map(str, accuracies))}")
