def draw_cards(*args, **kwargs):
    monsters = []
    spells = []
    output = []

    for name_of_card, type_of_card in args:
        if type_of_card == 'monster':
            monsters.append(name_of_card)
        elif type_of_card == 'spell':
            spells.append(name_of_card)

    for card in kwargs:
        if kwargs[card] == 'spell':
            spells.append(card)
        elif kwargs[card] == 'monster':
            monsters.append(card)


    if monsters:
        output.append("Monster cards:")
        for card in sorted(monsters, reverse=True):
            output.append(f"  ***{card}")

    if spells:
        output.append("Spell cards:")
        for card in sorted(spells):
            output.append(f"  $$${card}")


    return '\n'.join(output)


print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))