from collections import deque

packages = [int(x) for x in input().split()] #stack
couriers = deque([int(x) for x in input().split()]) #queue

total_weight_delivered = 0
while packages and couriers:
    curr_package = packages[-1]
    curr_courier = couriers[0]

    if curr_courier > curr_package:
        # Courier can deliver with capacity to spare
        curr_courier -= curr_package * 2
        if curr_courier > 0:
            couriers.append(curr_courier)
        couriers.popleft()
        total_weight_delivered += curr_package
        packages.pop()
    elif curr_courier == curr_package:
        # Exact match - both are removed
        couriers.popleft()
        total_weight_delivered += curr_package
        packages.pop()
    else:
        # Partial delivery
        curr_package -= curr_courier
        couriers.popleft()
        packages[-1] = curr_package
        total_weight_delivered += curr_courier



print(f"Total weight: {total_weight_delivered} kg")
if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
if packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages))}")
if not packages and couriers:
    print(f"Couriers are still on duty: {', '.join(map(str, couriers))} but there are no more packages to deliver.")





