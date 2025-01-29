with open("text.txt") as f:
    # Split lines into a list:
    content = f.read().splitlines()

    for i in range(len(content)):
        line = content[i]

        # Summing letter and punctuation count:
        letter_count = sum(1 for ch in line if ch.isalpha())
        punctuation_count = sum(1 for ch in line if ch in ["-", ",", ".", "!", "?", "'"])

        # Print info:
        print(f"Line {i + 1}: {line} ({letter_count})({punctuation_count})")
