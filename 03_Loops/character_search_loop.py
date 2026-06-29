while True:
	try:
		user_str = input("Enter a string: ")
		user_chr = input("Enter a character: ")		
		if user_chr in user_str:
			print("The character is in the string.")
		else:
			print("The character is not in the string.")
		again = input("Do you want to try again (y/n)? ")
		if again != "y":
			print("Goodbye")
			break
	except ValueError:
		print("Invalid input.")

