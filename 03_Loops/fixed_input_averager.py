repeat = "yes"

while repeat.lower() == "yes":
	number = []
	i = 0
	while i < 10:
		try:
			num_list = float(input(f"Enter number {i+1}: "))					
			number.append(num_list)		
			i += 1
		except ValueError:
			print("Invalid input.")
	average = sum(number) / len(number)
	print(f"Your average numbers is {average:.2f}")
	repeat = input("Would you like to repeat? (yes/no): ")
print("Loop ends.")