while True:
    try:
        print("------Jolly McTucky------")
        print("[1] Meals")
        print("[2] Pasta")
        print("[3] Burger")
        print("[4] Dessert")
        print("[5] Drinks")
        print("[0] Exit")
        choice = input("CHOICE: ")

        def meals():
            print("------MEALS------")
            print("[A] 1 piece chicken with rice")
            print("[B] 2 pieces chicken with rice")
            print("[C] 3 pieces chicken")
            print("[D] 6 pieces chicken")
            print("[E] 8 pieces chicken")
            print("[X] Exit")
            meal_input = input("CHOICE: ")
            meal_choice = meal_input.upper()
            match meal_choice:
                case 'A': price = 110.0
                case 'B': price = 150.0
                case 'C': price = 200.0
                case 'D': price = 450.0
                case 'E': price = 650.0
                case 'X': 
                    print("Thank you for visiting Jolly McTucky")
                    return 
                case _: 
                    print("Invalid Choice")
                    return
            try:
                quantity = int(input("Quantitiy? "))
                total = price * quantity
                print(f"Your order total is {total}")
                pay = float(input("Amount Tendered: "))
                if pay < total:
                    print("Insufficient cash")
                else:
                    print("Your change is", pay - total)
            except ValueError:
                print("Invalid Input")  

        def pasta():
            print("------PASTA------")
            print("[A] Sphagetti")
            print("[B] Carbonara")
            print("[C] Mac & Cheese")
            print("[X] Exit")
            pasta_input = input("CHOICE: ")
            pasta_choice = pasta_input.upper()
            match pasta_choice:
                case 'A': price = 100.0
                case 'B': price = 110.0
                case 'C': price = 105.0
                case 'X': 
                    print("Thank you for visiting Jolly Jabez")
                    return 
                case _:
                    print("Invalid Choice")
                    return
            try:
                quantity = int(input("Quantitiy? "))
                total = price * quantity
                print(f"Your order total is {total}")
                pay = float(input("Amount Tendered: "))
                if pay < total:
                    print("Insufficient cash")
                else:
                    print("Your change is", pay - total)
            except ValueError:
                print("Invalid Input")
        
        def burger():
            print("------BURGER------")
            print("[A] Classic Hamburger")
            print("[B] Cheesebruger")
            print("[C] Bacon Cheeseburger")
            print("[D] Double Patty burger")
            print("[X] Exit")
            burger_input = input("CHOICE: ")
            burger_choice = burger_input.upper()
            match burger_choice:
                case 'A': price = 89.0
                case 'B': price = 99.0
                case 'C': price = 119.0
                case 'D': price = 139.0
                case 'X': 
                    print("Thank you for visiting Jolly McTucky")
                    return 
                case _:
                    print("Invalid Jabez")
                    return
            try:
                quantity = int(input("Quantitiy? "))
                total = price * quantity
                print(f"Your order total is {total}")
                pay = float(input("Amount Tendered: "))
                if pay < total:
                   print("Insufficient cash")
                else:
                 print("Your change is", pay - total)
            except ValueError:
                print("Invalid Input")

        def dessert():
            print("------DESSERT------")
            print("[A] Chocolate Cake")
            print("[B] Ice Cream Sundae")
            print("[C] Cheesecake")
            print("[X] Exit")
            dessert_input = input("CHOICE: ")
            dessert_choice = dessert_input.upper()
            match dessert_choice:
                case 'A': price = 89.0
                case 'B': price = 65.0
                case 'C': price = 95.0
                case 'X': 
                    print("Thank you for visiting Jolly McTucky")
                    return 
                case _:
                    print("Invalid Choice")
                    return
            try:
                quantity = int(input("Quantitiy? "))
                total = price * quantity 
                print(f"Your order total is {total}")
                pay = float(input("Amount Tendered: "))
                if pay < total:
                    print("Insufficient cash")
                else:
                    print("Your change is", pay - total)
            except ValueError:
                print("Invalid Input")
    
        def drinks():
            print("------DRINKS------")
            print("[A] Ice Tea")
            print("[B] Soft Drinks")
            print("[C] Lemonade")
            print("[X] Exit")
            drinks_input = input("CHOICE: ")
            drinks_choice = drinks_input.upper()
            match drinks_choice:
                case 'A': price = 35.0
                case 'B': price = 45.0
                case 'C': price = 40.0
                case 'X': 
                    print("Thank you for visiting Jolly McTucky")
                    return 
                case _:
                    print("Invalid Choice")
                    return
            try:
                quantity = int(input("Quantitiy? "))
                total = price * quantity
                print(f"Your order total is {total}")
                pay = float(input("Amount Tendered: "))
                if pay < total:
                    print("Insufficient cash")
                else:
                    print("Your change is", pay - total)
            except ValueError:
                print("Invalid Input")
        match choice:
            case '1':
                meals()
            case '2':
                pasta()
            case'3':
                burger()
            case '4':
                dessert()
            case '5':
                drinks()
            case '0':
                print("Thank you for visiting Jolly McTucky")
                break
            case _:
                print("Invalid Choice")
        repeat = input("Do you want to try again? (y/n): ").lower()
        while repeat != 'y' and repeat != 'n':
            print("Invalid Input. Enter \'y\' or \'n\'")
            repeat = input("Do you want to try again? (y/n): ")
        if repeat.casefold() == 'n':
            exit()
    except ValueError:
        print("Invalid Input")

        
