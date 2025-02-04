def cookbook(*args):
    cuisines = {}
    output = []

    for recipe_name, cuisine, ingredients in args:
        if cuisine not in cuisines:
            cuisines[cuisine] = {}
        cuisines[cuisine][recipe_name] = ingredients


    for cuisine, recipes in sorted(cuisines.items(), key=lambda x: (-len(x[1]), x[0])):
        output.append(f"{cuisine} cuisine contains {len(recipes)} recipes:\n")
        for recipe_name, ingredients in sorted(recipes.items()):
            output.append(f"  * {recipe_name} -> Ingredients: {', '.join(ingredients)}\n")


    return ''.join(output)

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
