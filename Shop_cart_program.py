foods = []
prices = []
total = 0

while 1:
    food = input("Enter food You want to buy:")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter Price of {food}:"))
        foods.append(food)
        prices.append(price)

print("---Your cart---")
for i in foods:
    print(i, end="|")
print()
for j in prices:
    total += j
print(f"Total Bill:{total}")
