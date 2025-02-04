def boarding_passengers(capacity, *passenger_groups):
    boarded = {}
    output = []

    # Create a list of passenger groups for easier manipulation
    groups = list(passenger_groups)

    # Board passengers while there is capacity
    while capacity > 0:
        # Flag to check if any group was boarded in this iteration
        boarded_any = False

        for i, (passengers, program_name) in enumerate(groups):
            if passengers <= capacity:
                if program_name not in boarded:
                    boarded[program_name] = 0
                boarded[program_name] += passengers
                capacity -= passengers
                # Remove the boarded group from the list
                groups[i] = (0, program_name)  # Mark as boarded
                boarded_any = True

        # If no group was boarded in this iteration, break the loop
        if not boarded_any:
            break

    # Prepare the output
    output.append("Boarding details by benefit plan:")
    for program, count_of_passengers in sorted(boarded.items(), key=lambda x: (-x[1], x[0])):
        output.append(f"## {program}: {count_of_passengers} guests")

    # Calculate total passengers boarded
    total_boarded = sum(boarded.values())
    total_passengers = sum(passengers for passengers, _ in passenger_groups)

    # Determine the final message
    if total_boarded == total_passengers:
        output.append("All passengers are successfully boarded!")
    elif capacity == 0 and total_boarded < total_passengers:
        output.append("Boarding unsuccessful. Cruise ship at full capacity.")
    else:
        output.append(f"Partial boarding completed. Available capacity: {capacity}.")

    return '\n'.join(output)


print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))