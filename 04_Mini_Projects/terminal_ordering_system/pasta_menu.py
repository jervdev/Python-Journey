def pasta():
    global menu
    print("---- Pasta ----")
    pstamenu = ["[A] Alfredo Pasta", "[B] Carbonara Pasta", "[C] Fusili Pasta", "[D] Bucatini Pasta"]
    pstaprice = [60, 70, 80, 90]
    menu = pstaprice
    for i in pstamenu:
        print(i)