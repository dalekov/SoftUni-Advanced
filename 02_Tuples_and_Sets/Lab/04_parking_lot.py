n = int(input())

parking_lot = set()

for i in range(n):
    direction, car_number = input().split(', ')

    if direction == 'IN':
        parking_lot.add(car_number)
    elif direction == 'OUT':
        parking_lot.discard(car_number)

if parking_lot:
    print('\n'.join(parking_lot))
else:
    print("Parking Lot is Empty")
