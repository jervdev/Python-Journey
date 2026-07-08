menu = []

def titlepage():
    print("\n---- McJolly ----")
    print("[1] Meals\n[2] Pasta\n[3] Burger\n[4] Dessert\n[5] Drinks\n[0] Exit")

import meals_menu

import pasta_menu

import burger_menu

import dessert_menu

import drinks_menu

def ordercalc(order):
    global menu
    try:
        qty = int(input("Quantity?: "))
        total = menu[order] * qty
        print(f"Your order total is: PHP {total:.2f}")
        cash = int(input("Amount Tendered: "))
        change = cash - total
        if change >= 0:
            print(f"Your change is PHP {change:.2f}")
        else:
            print("Not enough cash. Try again.")
    except ValueError:
        print("Invalid input. Try again.")

while True:
    titlepage()
    try:
        usermenu = int(input("CHOICE: "))
    except ValueError:
        print("Invalid input.")
        continue

    if usermenu == 0:
        print("Thank you for visiting McJolly!")
        break

    match usermenu:
        case 1:
            while True:
                meals_menu.meals()
                menu = meals_menu.menu
                choice = input("CHOICE: ").upper()
                match choice:
                    case 'A': ordercalc(0)
                    case 'B': ordercalc(1)
                    case 'C': ordercalc(2)
                    case 'D': ordercalc(3)
                repeat = input("Would you like anything else? (y/n): ")
                if repeat.lower() != 'y':
                    print("Thank you for visiting McJolly!")
                    exit()

        case 2:
            while True:
                pasta_menu.pasta()
                menu = pasta_menu.menu
                choice = input("CHOICE: ").upper()
                match choice:
                    case 'A': ordercalc(0)
                    case 'B': ordercalc(1)
                    case 'C': ordercalc(2)
                    case 'D': ordercalc(3)
                repeat = input("Would you like anything else? (y/n): ")
                if repeat.lower() != 'y':
                    print("Thank you for visiting McJolly!")
                    exit()

        case 3:
            while True:
                burger_menu.burger()
                menu = burger_menu.menu
                choice = input("CHOICE: ").upper()
                match choice:
                    case 'A': ordercalc(0)
                    case 'B': ordercalc(1)
                    case 'C': ordercalc(2)
                    case 'D': ordercalc(3)
                repeat = input("Would you like anything else? (y/n): ")
                if repeat.lower() != 'y':
                    print("Thank you for visiting McJolly!")
                    exit()

        case 4:
            while True:
                dessert_menu.dessert()
                menu = dessert_menu.menu
                choice = input("CHOICE: ").upper()
                match choice:
                    case 'A': ordercalc(0)
                    case 'B': ordercalc(1)
                    case 'C': ordercalc(2)
                    case 'D': ordercalc(3)
                repeat = input("Would you like anything else? (y/n): ")
                if repeat.lower() != 'y':
                    print("Thank you for visiting McJolly!")
                    exit()

        case 5:
            while True:
                drinks_menu.drinks()
                menu = drinks_menu.menu
                choice = input("CHOICE: ").upper()
                match choice:
                    case 'A': ordercalc(0)
                    case 'B': ordercalc(1)
                    case 'C': ordercalc(2)
                    case 'D': ordercalc(3)
                repeat = input("Would you like anything else? (y/n): ")
                if repeat.lower() != 'y':
                    print("Thank you for visiting McJolly!")
                    exit()

        case _:
            print("Invalid choice.")
