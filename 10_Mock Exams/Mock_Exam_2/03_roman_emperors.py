def list_roman_emperors(*args, **kwargs):
    successful_emperors = {name: kwargs[name] for name, status in args if status}
    unsuccessful_emperors = {name: kwargs[name] for name, status in args if not status}

    output = []
    output.append(f"Total number of emperors: {len(args)}")
    if successful_emperors:
        output.append("Successful emperors:")
        for name, rule in sorted(successful_emperors.items(), key=lambda x: (-x[1], x[0])):
            output.append(f"****{name}: {rule}")

    if unsuccessful_emperors:
        output.append("Unsuccessful emperors:")
        for name, rule in sorted(unsuccessful_emperors.items(), key=lambda x: (x[1], x[0])):
            output.append(f"****{name}: {rule}")


    return '\n'.join(output)

print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))