def even_odd_filter(**kwargs):
    for key, value in kwargs.items():
        if key == 'odd':
            kwargs[key] = [num for num in value if num % 2 == 1]  # Keep only odd numbers
        elif key == 'even':
            kwargs[key] = [num for num in value if num % 2 == 0]  # Keep only even numbers

    return {key: value for key, value in sorted(kwargs.items(), key=lambda x: -len(x[1]))}


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2]
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
