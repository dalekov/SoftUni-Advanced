def operate(operator, *args):
    if operator == '+':
        return sum(args)
    elif operator == '-':
        total = args[0]
        for arg in args[1:]:
            total -= arg
    elif operator == '*':
        total = 1
        for arg in args:
            total *= arg
    elif operator == '/':
        total = args[0]
        for arg in args[1:]:
            if arg != 0:
                total /= arg

    return total

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 3, 0))
print(operate("*", 3, 4))
