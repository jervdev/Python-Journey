number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if number1 > number2:
	print("Number 1 is a bigger number and number 2 is smaller")
else:
	print("Number 2 is a bigger number and number 1 is smaller")

#2
number = int(input("Enter a number to determine if a number is odd or even: "))
if number % 2 == 0:
	print("Number is Even")
else:
	print("Number is Odd")