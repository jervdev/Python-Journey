while True:
	try:
		table = int(input("Kindly give a range for your multiplication table: "))
		ast = "*" * 20
		print(f"\n{ast}MULTIPLICATION TABLE{ast}\n")
		for i in range(1, table + 1):
			for j in range(1, table +1):
				expression = i * j
				print(f"{expression:>4}", end=" ")
			print()
	except ValueError:
		print("Error")
	loop = input("Would you like to repeat? (y/n): ")
	if loop != "y":
		print("Program Ends.")
		break
		