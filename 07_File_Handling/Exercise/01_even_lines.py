with open("text.txt") as f:
    content = f.read().split('\n')

    for i in range(len(content)):
        line = content[i]
        if i % 2 == 0: # Only even lines:

            # Replace characters:
            for ch in ["-", ",", ".", "!", "?"]:
                line = line.replace(ch, "@")

            # Reverse words and print
            print(" ".join(line.split()[::-1]))
