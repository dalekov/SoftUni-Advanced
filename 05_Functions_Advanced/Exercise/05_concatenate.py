def concatenate(*args, **kwargs):
    string = ''.join(args)

    for kwarg, value in kwargs.items():
        string = string.replace(kwarg, value)

    return string


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))