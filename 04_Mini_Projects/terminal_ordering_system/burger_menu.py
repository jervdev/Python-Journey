def burger():
    global menu
    print("---- Burger ----")
    brgrmenu = ["[A] Regular Burger", "[B] Double Patty Burger", "[C] Cheeseburger", "[D] Big Burger"]
    brgrprice = [40, 50, 50, 60]
    menu = brgrprice
    for i in brgrmenu:
        print(i)