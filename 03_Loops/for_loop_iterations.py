#using for loop to input elements in a list
#first solution
my_list = []
num_elements = int(input("Enter the number of elements: "))

for i in range(num_elements):
    item = input(f"Enter element {i+1}: ")
    my_list.append(item)

print("Your list:", my_list)
print("\n")


#second solution
num_elements = int(input("Enter the number of elements: "))
my_list = [input(f"Enter element {i+1}: ") for i in range(num_elements)]

print("Your list:", my_list)
print("\n\n\n")


#using for loop to print each character in a string
my_string = "Except"
strLen = len(my_string)
print(f"The string is {my_string} and its length is {strLen}")
for char in my_string:
    print(char)

print("\n")


#using for loop to print the index and the character in the index
my_string = "Negative"
for i in range(len(my_string)):
    print(f"Character at index {i}: {my_string[i]}")

print("\n")

#printing the index and the character seprarately
my_string = "java SCRIPT"
for index, char in enumerate(my_string):
    print(f"Index: {index}, Character: {char}")

print("\n")

my_string = input("Input a string: ")
for index, char in enumerate(my_string):
    print(f"Index: {index}, Character: {char}")

