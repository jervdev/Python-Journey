repeater = "y"

while repeater.lower() == "y":
	try:
		fibo_seq = int(input("Enter a number for the length of your Fibonacci Sequence: "))
		if fibo_seq <= 0:
			print("Enter a positive number")
		else:
			seq_one = 0
			seq_two = 1
			for i in range(fibo_seq):
				print(seq_one, end=" ")
				seq = seq_one + seq_two
				seq_one = seq_two
				seq_two = seq
			repeater = input("\nWould you like to repeat? (y/n): ")
	except ValueError:
		print("Invalid input.")
print("End of program.")