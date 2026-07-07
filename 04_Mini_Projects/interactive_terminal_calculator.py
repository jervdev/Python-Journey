while True:
	try:
		print("-------CALCULATOR-------")
		print("[1] Addition")
		print("[2] Subtraction")
		print("[3] Multiplication")		
		print("[4] Division")
		print("[0] Exit")
		choice_one = input("Choice: ")
		
		def addition():
			print("-------Addition-------")
			num1 = int(input("Give First Number: "))
			num2 = int(input("Give Second Number: "))
			print("Sum of numbers is", num1 + num2)
		def subtraction():
			print("-------Subtraction-------")
			num1 = int(input("Give First Number: "))
			num2 = int(input("Give Second Number: "))
			print("Difference of numbers is", num1 - num2)
		def multiplication():
			print("-------Multiplication-------")
			num1 = int(input("Give First Number: "))
			num2 = int(input("Give Second Number: "))
			print("Product of numbers is", num1 * num2)
		def division():
			print("-------Division-------")
			num1 = int(input("Give First Number: "))
			num2 = int(input("Give Second Number: "))
			print("Quotient of numbers is", num1 / num2)
		if choice_one == '0':
			print("Thank you for using Calculator")
			break
				
		if choice_one == '1':
			addition()
			repeat = input("Do you want to try again? ")
			if repeat.casefold() == 'n':
				break
		if choice_one == '2':
			subtraction()
			repeat = input("Do you want to try again? ")
			if repeat.casefold() == 'n':
				break
		if choice_one == '3':
			multiplication()
			repeat = input("Do you want to try again? ")
			if repeat.casefold() == 'n':
				break
		if choice_one == '4':
			division()
			repeat = input("Do you want to try again? ")
			if repeat.casefold() == 'n':
				break
		else:
			print("Invalid Choice")
				
	except ZeroDivisionError:
		print("\nError")
