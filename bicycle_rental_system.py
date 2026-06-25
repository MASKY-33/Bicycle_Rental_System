# P.S.) Building this Project-System really took me mentally deep for a whole afternoon until the next morning to get it fully working.
# It was so terrible that it was amazing!
# It was purely because I was searching for the correct System-architecture (flows), for making it work correcty.


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
