def drinks():
    global menu
    print("---- Drinks ----")
    drnkmenu = ["[A] Coke Zero ", "[B] Coke ", "[C] Iced Tea", "[D] Root Beer"]
    drnkprice = [40, 40, 40, 50]
    menu = drnkprice
    for i in drnkmenu:
        print(i)
