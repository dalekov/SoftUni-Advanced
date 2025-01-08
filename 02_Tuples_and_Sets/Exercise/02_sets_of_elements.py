n, m = input().split()

set_1 = set()
set_2 = set()

for i in range(int(n)):
    number = int(input())
    set_1.add(number)


for j in range(int(m)):
    number = int(input())
    set_2.add(number)

intersection = set_1.intersection(set_2)
for num in intersection:
    print(num)