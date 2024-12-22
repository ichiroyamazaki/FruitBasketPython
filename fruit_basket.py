basket = []
basket_container = {"a": "Apple", "o": "Orange", "m": "Mango", "g": "Guava"}

print("Catch and eat any of these fruits:('apple', 'orange', 'mango', 'guava')")
fruits = int(input("How many fruits would you like to catch? "))
print("Choose a fruit to catch. Press A, O, M or G.")

for i in range(fruits):
    fruitNumber = input("Fruit " + str(i + 1) + " of " + str(fruits) + ":")
    basket.append(basket_container[fruitNumber.lower()])

print("Your basket now has :", basket)
print("Press E to eat Fruit : ")

while True:
    eats = input()
    if eats.lower() == 'e':
        basket.pop()
        if not basket:
            print("No more Fruits.")
            break

    print("Your basket now has :", basket)
    print("Press E to eat Fruit : ")
