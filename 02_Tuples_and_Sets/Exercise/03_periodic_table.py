n = int(input())

unique = set()

for i in range(n):
    compounds = input().split()
    for compound in compounds:
        unique.add(compound)

for compound in unique:
    print(compound)