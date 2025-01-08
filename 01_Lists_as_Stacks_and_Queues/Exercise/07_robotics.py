from collections import deque
from datetime import datetime, timedelta


line  = input().split(';')
start_time = input()

# Parse start time
start_time = datetime.strptime(start_time, '%H:%M:%S')

# Parse robots
robots = []
for robot in line:
    name, process_time = robot.split('-')
    robots.append({"name": name, "process_time": int(process_time), "available_after": 0})

# Products queue
products = deque()
while True:
    product = input()

    if product == 'End':
        break

    products.append(product)

# Processing loop:
current_time = 0
while products:
    current_time += 1

    current_time_formatted = start_time + timedelta(seconds=current_time)
    product_assigned = False
    for robot in robots:
        if current_time >= robot["available_after"]:
            product = products.popleft()
            print(f'{robot["name"]} - {product} [{current_time_formatted.strftime("%H:%M:%S")}]')
            robot["available_after"] = current_time + robot["process_time"]
            product_assigned = True
            break

    if not product_assigned:
        products.append(products.popleft())