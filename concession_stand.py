menu = {
    "popcorn": 5.00,
    "candy": 2.50,
    "soda": 3.00,
    "pizza": 10.00,
    "nachos": 4.00,
    "hot dog": 4.00,
    "ice cream": 3.50
}

cart = []
total = 0

print("----------MENU----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------")

while True:
    food = input("Select an item (Q to quit): ").lower()

    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---------- YOUR ORDER ----------")

for food in cart:
    total += menu[food]
    print(food)

print()
print(f"Total is: ${total:.2f}")
