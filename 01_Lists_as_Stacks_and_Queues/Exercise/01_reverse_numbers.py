integers = input().split()

reversed_integers = []

for integer in integers[:]:
    reversed_integers.append(integers.pop())

print(' '.join(reversed_integers))