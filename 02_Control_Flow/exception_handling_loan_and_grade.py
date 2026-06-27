try:
	salary = int(input("Input your salary "))

	if salary >= 30000:
		years_on_the_job = int(input("Input your years on the job "))
		if years_on_the_job >= 2:
			print("You are qualified for the highest loan.")
		else:
			print("You must have been on your current job for at least two years to qualify.")
	if ((salary >= 15000) and (salary <= 29000)):
		years_on_the_job = int(input("Input your years on the job "))
		if years_on_the_job >= 2:
			print("You are qualified for the lower-range loan.")
		else:
			print("You must have been on your current job for at least two years to qualify.")
	else:
		print("You must earn at least $30,000 per year to qualify.")

except ValueError:
	print("That is an invalid input.")


print("\n********************************************End of first problem.********************************************\n")

try:
	grade = int(input("Input your grade "))

	if grade >= 90:
		if (grade >= 96) and (grade <= 100):
			print("Your grade is A+.")
		elif (grade >= 92) and (grade <= 95):
			print("Your grade is A.")
		else:
			print("Your grade is A-.")
	elif grade >= 80:
		if (grade >= 86) and (grade <= 89):
			print("Your grade is B+.")
		elif (grade >= 82) and (grade <= 85):
			print("Your grade is B.")
		else:
			print("Your grade is B-.")
	elif grade >= 70:
		if (grade >= 76) and (grade <= 79):
			print("Your grade is C+.")
		elif (grade >= 72) and (grade <= 75):
			print("Your grade is C.")
		else:
			print("Your grade is C-.")
	elif grade >= 60:
		if (grade >= 66) and (grade <= 69):
			print("Your grade is D+.")
		elif (grade >= 62) and (grade <= 65):
			print("Your grade is D.")
		else:
			print("Your grade is D-.")
	else:
		print("Your grade is F.")
except ValueError:
	print("That is an invalid input.")

print("\n********************************************End of second problem.********************************************\n")