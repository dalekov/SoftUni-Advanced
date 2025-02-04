def plant_garden(available_space, *allowed_plants, **requested_plants):
    allowed_dict = dict(allowed_plants)  # Convert allowed plants into a dictionary
    planted = {}

    for plant in sorted(requested_plants.keys()):  # Sort requested plants alphabetically
        if plant in allowed_dict:  # Check if the plant is allowed
            space_required = allowed_dict[plant]
            requested_pieces = requested_plants[plant]

            # Check how many pieces can be planted
            max_possible = available_space // space_required
            pieces_to_plant = min(requested_pieces, int(max_possible))

            if pieces_to_plant > 0:
                planted[plant] = pieces_to_plant
                available_space -= pieces_to_plant * space_required

    # Determine final message
    if all(requested_plants[plant] == planted.get(plant, 0) for plant in requested_plants if plant in allowed_dict):
        result = [f"All plants were planted! Available garden space: {available_space:.1f} sq meters."]
    else:
        result = ["Not enough space to plant all requested plants!"]

    # Append planted plants
    result.append("Planted plants:")
    for plant in sorted(planted.keys()):
        result.append(f"{plant}: {planted[plant]}")

    return "\n".join(result)


print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))