salary = int(input("Input your salary "))

if salary >= 30000:
	years_on_the_job = int(input("Input your years on the job "))
	if years_on_the_job >= 2:
		print("You qualify for loan.")
	else:
		print("You must have been on your current job for at least two years to qualify.")
else:
	print("You must earn at least $30,000 per year to qualify.")


grade = int(input("Input your grade "))

if grade >= 90:
	print("Your grade is A.")
elif grade >= 80:
	print("Your grade is B.")
elif grade >= 70:
	print("Your grade is C.")
elif grade >= 60:
	print("Your grade is D.")
else:
	print("Your grade is F.")

