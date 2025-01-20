def multiply(*args):
    total = 1
    for arg in args:
        total *= arg

    return total

print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
