while True:
    line = input().split('-')

    if line[0] == 'End':
        break

    command, file_name = line[0], line[1]
    if command == 'Create':
        open(file_name, 'w').close() # Creates or clears the file

    elif command == 'Add':
        content = line[2]
        with open(file_name, 'a') as f:
            f.write(content + '\n')

    elif command == 'Replace':
        old_string, new_string = line[2], line[3]
        try:
            with open(file_name, 'r') as f:
                content = f.read()
            content = content.replace(old_string, new_string)
            with open(file_name, 'w') as f:
                f.write(content)
        except FileNotFoundError:
            print("An error occurred")

    elif command == 'Delete':
        import os
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")
