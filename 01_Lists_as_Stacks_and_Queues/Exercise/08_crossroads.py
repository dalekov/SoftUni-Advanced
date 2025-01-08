from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

queue = deque()

total_cars_passed = 0
while True:
    command = input()

    if command == 'END':
        print("Everyone is safe.")
        print(f"{total_cars_passed} total cars passed the crossroads.")
        break

    elif command == 'green':
        total_time = green_light_duration
        while queue and total_time > 0:
            car = queue.popleft()
            car_length = len(car)

            if total_time >= car_length:
                total_time -= car_length
                total_cars_passed += 1
            else:
                total_time += free_window_duration

                if total_time >= car_length:
                    total_cars_passed += 1
                    break
                else:
                    crash_point = car[total_time]
                    print("A crash happened!")
                    print(f"{car} was hit at {crash_point}.")
                    exit()
    else:
        queue.append(command)

