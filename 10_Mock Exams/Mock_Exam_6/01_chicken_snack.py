from collections import deque

money = [int(x) for x in input().split()] #stack
prices = deque([int(x) for x in input().split()]) #queue

food_eaten = 0
while money and prices:
    curr_money = money[-1]
    curr_price = prices[0]

    if curr_money == curr_price:
        money.pop()
        prices.popleft()
        food_eaten += 1

    elif curr_money > curr_price:
        change = curr_money - curr_price
        money.pop()
        if not money:
            money.append(0)
        money[-1] += change
        prices.popleft()
        food_eaten += 1
    elif curr_money < curr_price:
        prices.popleft()
        money.pop()


if food_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {food_eaten} foods.")
elif food_eaten > 0:
    if food_eaten == 1:
        print(f"Henry ate: {food_eaten} food.")
    else:
        print(f"Henry ate: {food_eaten} foods.")
elif food_eaten == 0:
    print("Henry remained hungry. He will try next weekend again.")

