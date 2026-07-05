END = -1000 

print("Enter numbers to sum, or enter", END, "to quit.")

total_sum = 0
while True:
    try:
        user_input = int(input("Input a number: "))
        if user_input == END:
            break 
        total_sum += user_input
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("The sum of the entered numbers is:", total_sum)


print("\nNext program")

sum = 0
data = int(input("How long? (enter -100 to end) "))
while data != -100:
    sum = sum + data
    data = int(input("How long? (enter -100 to end) "))
print("Sum:",sum)


for i in range(10):
	print(i)


for i in range(3):  
	for j in range(2): 
		print(f"Outer: {i}, Inner: {j}")

print("\nNext program")

adj = ["Bland", "Bad", "Yummy"]
food = ["Steak", "Pork", "Chicken"]

for x in adj:
	for y in food:
		print(x, y)


print("\nNext program")

outer_counter = 0
while outer_counter < 3:
	print(f"Outer loop: {outer_counter}")
	inner_counter = 0 
	while inner_counter < 2:
		print(f"  Inner loop: {inner_counter}")
		inner_counter += 1
        
	outer_counter += 1

print("\nNext program")

for multiplicant in range(1, 15):
	for multiplier in range(1, 6):
		expression = f"{multiplicant:>2d} * {multiplier}"
		product = multiplicant * multiplier
		print(f"{expression} = {product:>2d}", end="\t")
	print()
