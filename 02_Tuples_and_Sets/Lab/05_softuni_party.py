n = int(input())

reservations = set()

for i in range(n):
    reservation_code = input()
    reservations.add(reservation_code)

while True:
    current_code = input()
    if current_code in reservations:
        reservations.remove(current_code)

    if current_code == 'END':
        reservations = sorted(reservations)
        print(len(reservations))
        for reservation in reservations:
            print(reservation)
        break
