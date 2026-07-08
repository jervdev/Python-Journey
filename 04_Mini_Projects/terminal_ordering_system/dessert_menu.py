def dessert():
    global menu
    print("---- Dessert ----")
    dsrtmenu = ["[A] Halo Halo", "[B] Ice Cream ", "[C] Leche Flan", "[D] Mais con yelo", "[E] Buko Pandan", "[F] Fruit Salad",]
    dsrtprice = [50, 30, 50, 25, 35, 35]
    menu = dsrtprice
    for i in dsrtmenu:
        print(i)
