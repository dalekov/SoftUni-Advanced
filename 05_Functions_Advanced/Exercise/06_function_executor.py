def func_executor(*args):
    output = []

    for func, func_args in args:
        result = func(*func_args)
        output.append(f"{func.__name__} - {result}")

    return '\n'.join(map(str, output))

def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))


