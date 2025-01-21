def age_assignment(*args, **kwargs):
    result = {name: kwargs[name[0]] for name in args}

    output = []
    for name, age in sorted(result.items(), key=lambda x: x[0]):
        output.append(f"{name} is {age} years old.")

    return '\n'.join(output)

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))