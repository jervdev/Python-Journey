try:
	num1 = int(input("Enter a number: "))
	num2 = int(input("Enter a another number: "))
	result = num1 / num2
	print(f"The result of division is: {result}")
except ValueError:
	print("Invalid input. Please enter a integer.")
except ZeroDivisionError:
	print("Error:  Cannot divide by zero.")
except Exception as e:
	print(f"An unexpected error occurred: (e).")
finally:
	print("Execution complete.")


try: 
	operator = input("Enter an operator: ")
	x = 5
	y = 10

	match operator:
		case '+': result = x + y
		case '-': result = x - y
		case '*': result = x * y
		case '/': result = x / y
		case _: result = "Invalid Operation"
	print(result)
except ValueError:
	print("Invalid input.")