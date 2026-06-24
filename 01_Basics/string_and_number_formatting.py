money = 50.02
tip = money * 0.50
print("The tip is ${:.2f}".format(tip))

print('{:,d}'.format(1000))

print("Hello \nWorld!")

print("Mabuhay \t Philippines")

print("{:<20s}".format("Hello World!"))
print("{:>20s}".format("Hello Universe!"))
print("{:^100s}".format("Hello Philippines!"))

name = input("\nInput your name")
print(f"Hello, {name}!")

Phi = 1.618
radius = float(input("\nPlease input the value for radius"))

area_circle = Phi*radius**2

print("Are of the circle is {:.2f}".format(area_circle))

N = float(input("Please give a number: "))
if (N>0):
	print("Is N>0?", N>0)
	print("Number is NEGATIVE")
else:
	print("Is N>0?", N>0)
	print("Number is POSITIVE")

