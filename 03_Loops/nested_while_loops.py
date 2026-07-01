myList = [4, 7, 9, 2, 5, 1]
while True:
	try:
		total = 0
		i = 0
		while i < len(myList):
			myList[i] = 0
			i += 1
		
		average = total / len(myList)
		print(f"The average is {average:.2f}")
	
		again = input("Do you want to repeat (y/n)? ")
		if again != "y":
			print("Loop ends.")
			break
	except ValueError:
		print("Error")