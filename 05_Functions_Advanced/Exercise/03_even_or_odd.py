def even_odd(*args) -> list:
    if args[-1] == 'even':
        return [num for num in args[:len(args) - 1] if num % 2 == 0]
    elif args[-1] == 'odd':
        return [num for num in args[:len(args) - 1] if num % 2 == 1]

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
