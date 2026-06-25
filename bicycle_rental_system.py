rentable_bicycles = {
    "stadsfiets" : 120.00,
    "e-bike" : 249.99,
    "mountainbike" : 70.00
}

while True:
    bicycle_search = input("Which bicycle are you searching for?: ").lower()

    if bicycle_search == "quit":
        print("Thankyou, goodbye!")
        break

    if bicycle_search in rentable_bicycles:
        bicycle_price = rentable_bicycles[bicycle_search]
        print(f"bicycle price is: {bicycle_price}")
    else:
        print("Bicycle is not available")
