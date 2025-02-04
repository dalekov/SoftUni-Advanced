def accommodate(*guest_groups, **room_info):
    no_accommodation = 0
    accommodated = {}

    output = []

    rooms = [(room, capacity) for room, capacity in sorted(room_info.items(), key=lambda x: (x[1], x[0]))]

    for guest_group_size in guest_groups:
        for room in rooms[:]:
            if room[1] >= guest_group_size:
                accommodated[room[0][5:]] = guest_group_size
                rooms.remove(room)
                break
        else:
            no_accommodation += guest_group_size


    if accommodated:
        output.append(f"A total of {len(accommodated)} accommodations were completed!")
        for room_number, guests in sorted(accommodated.items(), key=lambda x: x[0]):
            output.append(f"<Room {room_number} accommodates {guests} guests>")
    else:
        output.append("No accommodations were completed!")


    if no_accommodation:
        output.append(f"Guests with no accommodation: {no_accommodation}")

    empty_rooms = len(room_info) - len(accommodated)
    if empty_rooms:
        output.append(f"Empty rooms: {empty_rooms}")


    return '\n'.join(output)


print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))