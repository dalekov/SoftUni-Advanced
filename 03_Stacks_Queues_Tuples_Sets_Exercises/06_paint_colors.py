def find_colors(input_string):
    main_colors = {"red", "yellow", "blue"}
    secondary_colors = {"orange", "purple", "green"}
    secondary_color_requirements = {
        "orange": {"red", "yellow"},
        "purple": {"red", "blue"},
        "green": {"yellow", "blue"}
    }

    string = input_string.split()
    collected_colors = []

    while string:
        # Take the first and last substrings
        first = string.pop(0) if string else ""
        last = string.pop(-1) if string else ""

        # Combine them to check for colors
        combined = first + last
        reversed_combined = last + first

        if combined in main_colors or reversed_combined in main_colors:
            collected_colors.append(combined if combined in main_colors else reversed_combined)
        elif combined in secondary_colors or reversed_combined in secondary_colors:
            color = combined if combined in secondary_colors else reversed_combined
            # Check if the required primary colors are already in the result
            collected_colors.append(color)
        else:
            # Modify substrings and reinsert into the middle
            first = first[:-1]
            last = last[:-1]
            if first or last:
                middle = len(string) // 2 + (len(string) % 2)
                if last:
                    string.insert(middle, last)
                if first:
                    string.insert(middle, first)

    result = []
    main_colors_found = set(color for color in collected_colors if color in main_colors)

    for color in collected_colors:
        if color in main_colors:
            result.append(color)
        elif color in secondary_colors and secondary_color_requirements[color].issubset(main_colors_found):
            result.append(color)

    return result

# Example usage
input_string = input()
colors_found = find_colors(input_string)
print(colors_found)
